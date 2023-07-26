from werkzeug import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from user.views import User
from app import app 
from flask import Flask
app.register_blueprint(User)
application = DispatcherMiddleware(NotFound(), {
    "/prefix": app
})
if __name__ == "__main__":
    run_simple("0.0.0.0", 8000, application, use_reloader=True, threaded=True)
