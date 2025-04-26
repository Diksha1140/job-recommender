# app/models/job.py
class Job:
    def __init__(self, id, title, company, description, skills_required, location, salary_range=None):
        self.id = id
        self.title = title
        self.company = company
        self.description = description
        self.skills_required = skills_required  # List of skills
        self.location = location
        self.salary_range = salary_range  # Optional
        
    def __repr__(self):
        return f"<Job {self.id}: {self.title} at {self.company}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'description': self.description,
            'skills_required': self.skills_required,
            'location': self.location,
            'salary_range': self.salary_range
        }
