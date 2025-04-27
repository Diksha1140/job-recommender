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

## Deployment on Render
1. Create a Render account and link your GitHub repository.
2. Create a Web Service, select the repository, and set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -w 4 -b 0.0.0.0:8000 run:app`
3. Deploy and access at the provided `.onrender.com` URL.
