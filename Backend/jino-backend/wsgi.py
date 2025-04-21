from app import create_app  # Import create_app function from app/__init__.py

app = create_app()  # Create the app instance

if __name__ == "__main__":
    app.run()
