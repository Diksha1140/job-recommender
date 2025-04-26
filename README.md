# job-recommender
# Job Recommender System

A Flask-based web app that parses resumes, extracts skills using NLTK, and matches candidates to jobs.

## Setup
1. Clone: `git clone https://github.com/Diksha1140/job-recommender`
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Download NLTK data: `python -c "import nltk; nltk.download('punkt_tab'); nltk.download('stopwords')"`
6. Run: `python run.py`

## Features
- Resume upload (PDF/DOCX)
- Skill extraction with NLTK
- Job matching with percentage scores

## Technologies
- Python, Flask, NLTK, Gunicorn
