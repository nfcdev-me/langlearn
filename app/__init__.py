from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    
    # Configuration (can be moved to a config file)
    app.config['SECRET_KEY'] = '0a4e6131bd2a99f331297d0a3da6f9c7d6f3df7fa7a316fe'
    
    # Register Blueprints or routes
    app.register_blueprint(main)
    
    return app
