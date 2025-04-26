from flask import current_app
import os

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def save_uploaded_file(file):
    """Save an uploaded file to the configured upload folder"""
    if file and allowed_file(file.filename):
        # Create a safe filename
        from werkzeug.utils import secure_filename
        filename = secure_filename(file.filename)
        
        # Save the file
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        return filepath
    
    return None
