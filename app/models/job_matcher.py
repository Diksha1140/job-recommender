# app/services/job_matcher.py
class JobMatcher:
    def __init__(self, job_repository):
        self.job_repository = job_repository
    
    def match_jobs_by_skills(self, candidate_skills, num_results=10):
        """
        Match jobs based on candidate's skills
        Returns a list of (job, match_score) tuples sorted by relevance
        """
        # Convert all skills to lowercase for case-insensitive matching
        candidate_skills = [skill.lower() for skill in candidate_skills]
        
        matches = []
        
        for job in self.job_repository.get_all_jobs():
            job_skills = [skill.lower() for skill in job.skills_required]
            
            # Calculate match score
            common_skills = set(candidate_skills) & set(job_skills)
            match_percentage = len(common_skills) / len(job_skills) if job_skills else 0
            
            # Store tuple of (job, score, matching_skills)
            matches.append((
                job, 
                match_percentage, 
                list(common_skills)
            ))
        
        # Sort by match percentage (highest first)
        matches.sort(key=lambda x: x[1], reverse=True)
        
        # Return limited number of results
        return matches[:num_results]
