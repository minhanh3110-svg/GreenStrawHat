from flask import Flask
def create_app():
    app = Flask(__name__)
    from app.routes import auth, moi_truong
    app.register_blueprint(auth.bp)
    app.register_blueprint(moi_truong.bp)
    return app
