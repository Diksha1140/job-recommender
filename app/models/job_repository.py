# app/models/job_repository.py
import json
import os
from app.models.skjob import Job

class JobRepository:
    def __init__(self, job_data_folder):
        self.job_data_folder = job_data_folder
        self.jobs = []
        self._load_jobs()
    
    def _load_jobs(self):
        """Load jobs from JSON file or create default jobs if no file exists"""
        job_file = os.path.join(self.job_data_folder, 'jobs.json')
        
        if os.path.exists(job_file):
            try:
                with open(job_file, 'r') as f:
                    jobs_data = json.load(f)
                
                for job_data in jobs_data:
                    job = Job(
                        id=job_data['id'],
                        title=job_data['title'],
                        company=job_data['company'],
                        description=job_data['description'],
                        skills_required=job_data['skills_required'],
                        location=job_data['location'],
                        salary_range=job_data.get('salary_range')
                    )
                    self.jobs.append(job)
            except Exception as e:
                print(f"Error loading jobs: {e}")
                self._create_default_jobs()
        else:
            self._create_default_jobs()
            self._save_jobs()
    
    def _create_default_jobs(self):
        """Create some default jobs for testing"""
        default_jobs = [
            Job(
                id=1,
                title="Python Developer",
                company="Tech Innovations Inc.",
                description="Looking for an experienced Python developer to join our fast-paced team. The ideal candidate will have experience with web frameworks, RESTful APIs, and database design.",
                skills_required=["python", "django", "flask", "sql", "git", "aws"],
                location="Remote",
                salary_range="$90,000 - $120,000"
            ),
            Job(
                id=2,
                title="Data Scientist",
                company="Data Insights Co.",
                description="Seeking a data scientist to analyze complex datasets and develop machine learning models. Must have strong Python skills and experience with data visualization.",
                skills_required=["python", "machine learning", "data science", "sql", "tensorflow", "pandas"],
                location="New York, NY",
                salary_range="$110,000 - $140,000"
            ),
            Job(
                id=3,
                title="Java Backend Developer",
                company="Enterprise Solutions",
                description="Join our team to develop scalable backend services using Java. Experience with Spring Boot and microservices architecture is required.",
                skills_required=["java", "spring", "sql", "kubernetes", "docker", "ci/cd"],
                location="Chicago, IL",
                salary_range="$95,000 - $125,000"
            ),
            Job(
                id=4,
                title="DevOps Engineer",
                company="Cloud Systems Inc.",
                description="Looking for a DevOps engineer to automate deployment processes and manage cloud infrastructure. Experience with containerization and CI/CD pipelines is essential.",
                skills_required=["docker", "kubernetes", "jenkins", "aws", "git", "python", "ci/cd"],
                location="Remote",
                salary_range="$100,000 - $130,000"
            ),
            Job(
                id=5,
                title="Full Stack Developer",
                company="WebApp Creators",
                description="Seeking a versatile developer comfortable with both frontend and backend technologies. Must be able to work in an agile environment.",
                skills_required=["javascript", "react", "node", "python", "sql", "git", "agile"],
                location="San Francisco, CA",
                salary_range="$105,000 - $135,000"
            ),
            Job(
                id=6,
                title="Machine Learning Engineer",
                company="AI Innovations",
                description="Join our team to develop and deploy machine learning models for production use. Strong Python skills and experience with deep learning frameworks required.",
                skills_required=["python", "machine learning", "tensorflow", "pytorch", "docker", "git", "data science"],
                location="Boston, MA",
                salary_range="$115,000 - $150,000"
            )
        ]
        self.jobs = default_jobs
    
    def _save_jobs(self):
        """Save jobs to JSON file"""
        job_file = os.path.join(self.job_data_folder, 'jobs.json')
        os.makedirs(os.path.dirname(job_file), exist_ok=True)
        
        try:
            with open(job_file, 'w') as f:
                jobs_data = [job.to_dict() for job in self.jobs]
                json.dump(jobs_data, f, indent=2)
        except Exception as e:
            print(f"Error saving jobs: {e}")
    
    def get_all_jobs(self):
        """Return all jobs"""
        return self.jobs
    
    def get_job_by_id(self, job_id):
        """Get a job by its ID"""
        for job in self.jobs:
            if job.id == job_id:
                return job
        return None
    
    def add_job(self, job):
        """Add a new job"""
        # Generate a new ID if not provided
        if not job.id:
            job.id = max([j.id for j in self.jobs], default=0) + 1
        
        self.jobs.append(job)
        self._save_jobs()
        return job
