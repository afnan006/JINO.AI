from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from .routes import extract, context, reply
    app.register_blueprint(extract.extract_bp)
    app.register_blueprint(context.context_bp)
    app.register_blueprint(reply.reply_bp)


    # Health check route (optional but 🔥 for quick test)
    @app.route("/ping")
    def ping():
        return {"status": "JINO is alive and judging you 👀"}

    return app
