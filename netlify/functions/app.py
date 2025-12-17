"""
Netlify serverless function wrapper for Flask app
This adapts the Flask app to work with Netlify Functions (AWS Lambda)
"""
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

# Import the Flask app
from app import app

# Handler for Netlify Functions
def handler(event, context):
    """
    AWS Lambda handler for Netlify Functions
    """
    from serverless_wsgi import handle_request
    
    return handle_request(app, event, context)

