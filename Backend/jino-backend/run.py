

from app import create_app  # Import create_app from app/__init__.py
import os
from waitress import serve

# Create the app instance by calling create_app() from app
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port)  # Start the server with Waitress
