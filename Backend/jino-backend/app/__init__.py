# from flask import Flask
# from config import Config
# from flask_cors import CORS


# def create_app():
#     app = Flask(__name__)
#     CORS(app, resources={r"/*": {"origins": "*"}})  # Allow everything for now (dev only)
#     app.config.from_object(Config)

#     # Register blueprints
#     from .routes import extract, context, reply
#     app.register_blueprint(extract.extract_bp)
#     app.register_blueprint(context.context_bp)
#     app.register_blueprint(reply.reply_bp)


#     # Health check route (optional but 🔥 for quick test)
#     @app.route("/ping")
#     def ping():
#         return {"status": "JINO is alive and judging you 👀"}

#     # @app.route("/health")
#     return app

from flask import Flask
from config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Enable CORS - open to all origins (safe for dev, limit in prod)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://your-frontend.com"]}})
    
    # Load app config
    app.config.from_object(Config)

    # Register your blueprints
    from .routes import extract, context, reply
    app.register_blueprint(extract.extract_bp)
    app.register_blueprint(context.context_bp)
    app.register_blueprint(reply.reply_bp)

    # Health check route for Render & general vibes
    @app.route("/ping")
    def ping():
        return {"status": "JINO is alive and judging you 👀"}, 200

    # Optional: Add `/healthz` if Render expects this specific endpoint
    @app.route("/healthz")
    def healthz():
        return "ok", 200

    return app
