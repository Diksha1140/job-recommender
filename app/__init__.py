# app/__init__.py
from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = app.config['SECRET_KEY']  # Make sure this is here
    
    # Create upload directories if they don't exist
    import os
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['JOB_DATA_FOLDER'], exist_ok=True)
    
    # Register blueprints
    from app.routes.main_routes import main
    app.register_blueprint(main)
    
    return app
