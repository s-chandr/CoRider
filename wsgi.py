from werkzeug import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from user.views import User
from application import app,ping_app

app.register_blueprint(User)
application = DispatcherMiddleware(ping_app, {"/sme": app})

if __name__ == "__main__":
    run_simple("0.0.0.0", 8000, application, use_reloader=True, threaded=True)
