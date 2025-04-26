# In app/models/skill_extractor.py
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class SkillExtractor:
    def __init__(self):
        # Download required NLTK data
        try:
            # Make sure to download the correct resources
            nltk.download('punkt')
            nltk.download('stopwords')
            # No need for 'punkt_tab' - this appears to be an incorrect resource name
        except Exception as e:
            print(f"Error downloading NLTK resources: {e}")
        
        # A set of common technical skills (this would be expanded in a real system)
        self.skills_db = {
            'python', 'java', 'javascript', 'html', 'css', 'sql', 'nosql', 'react', 
            'angular', 'vue', 'node', 'express', 'django', 'flask', 'spring', 
            'bootstrap', 'jquery', 'aws', 'azure', 'gcp', 'docker', 'kubernetes',
            'jenkins', 'git', 'ci/cd', 'agile', 'scrum', 'devops', 'machine learning',
            'data science', 'tensorflow', 'pytorch', 'pandas', 'numpy', 'scikit-learn',
            'nlp', 'natural language processing', 'computer vision', 'ai', 'tableau',
            'power bi', 'excel', 'word', 'powerpoint', 'project management',
            'leadership', 'communication', 'collaboration', 'problem solving',
            'critical thinking', 'time management'
        }
    
    def extract(self, text):
        """Extract skills from text"""
        # Preprocess text
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Find skills without relying on tokenization first
        found_skills = []
        
        # Single word skills (simpler approach)
        words = text.split()
        for word in words:
            if word in self.skills_db:
                found_skills.append(word)
        
        # Multi-word skills
        for skill in self.skills_db:
            if ' ' in skill and skill in text:
                found_skills.append(skill)
        
        # Return unique skills
        return list(set(found_skills))
