# app/routes/main_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from werkzeug.utils import secure_filename
import os
from app.utils.file_handlers import allowed_file, save_uploaded_file
from app.models.resume_parser import ResumeParser
from app.models.skill_extractor import SkillExtractor
from app.models.job_repository import JobRepository
from app.models.job_matcher import JobMatcher

main = Blueprint('main', __name__)

# Create job repository instance
job_repo = None


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    print("Upload request received")
    
    if 'resume' not in request.files:
        print("No file part in request")
        flash('No file part', 'danger')
        return redirect(url_for('main.index'))
    
    file = request.files['resume']
    print(f"File received: {file.filename}")
    
    if file.filename == '':
        print("Empty filename")
        flash('No selected file', 'danger')
        return redirect(url_for('main.index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        print(f"Saving file to: {filepath}")
        file.save(filepath)
        
        # Process resume
        try:
            print("Starting resume parsing")
            parser = ResumeParser(filepath)
            resume_text = parser.extract_text()
            print(f"Text extracted, length: {len(resume_text)}")
            
            # Extract skills
            print("Starting skill extraction")
            skill_extractor = SkillExtractor()
            extracted_skills = skill_extractor.extract(resume_text)
            print(f"Skills extracted: {extracted_skills}")
            
            # Store in session for results page
            session['skills'] = extracted_skills
            
            # Match jobs
            global job_repo
            if job_repo is None:
                job_repo = JobRepository(current_app.config['JOB_DATA_FOLDER'])
            
            job_matcher = JobMatcher(job_repo)
            job_matches = job_matcher.match_jobs_by_skills(extracted_skills)
            
            # Store matches in session
            session['job_matches'] = [
                {
                    'job_id': match[0].id,
                    'title': match[0].title,
                    'company': match[0].company,
                    'match_percentage': int(match[1] * 100),
                    'matching_skills': match[2]
                }
                for match in job_matches if match[1] > 0
            ]
            
            return redirect(url_for('main.show_matches'))
            
        except Exception as e:
            print(f"Error processing file: {str(e)}")
            flash(f'Error processing file: {str(e)}', 'danger')
            return redirect(url_for('main.index'))
    
    print(f"Invalid file type: {file.filename}")
    flash('Invalid file type. Please upload a PDF or DOC/DOCX file.', 'danger')
    return redirect(url_for('main.index'))

@main.route('/skills')
def show_skills():
    skills = session.get('skills', [])
    return render_template('skills.html', skills=skills)

@main.route('/matches')
def show_matches():
    skills = session.get('skills', [])
    job_matches = session.get('job_matches', [])
    
    # Get detailed job information
    global job_repo
    if job_repo is None:
        job_repo = JobRepository(current_app.config['JOB_DATA_FOLDER'])
    
    detailed_matches = []
    for match in job_matches:
        job = job_repo.get_job_by_id(match['job_id'])
        if job:
            detailed_match = {
                'job': job,
                'match_percentage': match['match_percentage'],
                'matching_skills': match['matching_skills']
            }
            detailed_matches.append(detailed_match)
    
    return render_template('matches.html', skills=skills, matches=detailed_matches)

@main.route('/job/<int:job_id>')
def job_details(job_id):
    global job_repo
    if job_repo is None:
        job_repo = JobRepository(current_app.config['JOB_DATA_FOLDER'])
    
    job = job_repo.get_job_by_id(job_id)
    if not job:
        flash('Job not found', 'danger')
        return redirect(url_for('main.show_matches'))
    
    skills = session.get('skills', [])
    job_skills = job.skills_required
    matching_skills = list(set(skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(skills))
    
    return render_template('job_details.html', job=job, matching_skills=matching_skills, missing_skills=missing_skills)

