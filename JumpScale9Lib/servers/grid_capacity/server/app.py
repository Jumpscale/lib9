import sys

from flask import Flask, jsonify
from js9 import j
import os

from .nodes_api import nodes_api
from .farmers_api import farmers_api
from .frontend_blueprint import frontend_bp
from .flask_itsyouonline import configure
from . import settings


app = Flask(__name__)
app.secret_key = os.urandom(24)


configure(app, settings.IYO_CLIENTID, settings.IYO_SECRET, settings.IYO_CALLBACK, '/callback', None, True, True, 'organization')

app.register_blueprint(nodes_api)
app.register_blueprint(farmers_api)
app.register_blueprint(frontend_bp)
j.clients.mongoengine.get('capacity', interactive=False)


@app.errorhandler(500)
def internal_error(err):
    _, _, exc_traceback = sys.exc_info()
    eco = j.core.errorhandler.parsePythonExceptionObject(err, tb=exc_traceback)
    return jsonify(code=500, message=eco.errormessage, stack_trace=eco.traceback), 500


if __name__ == "__main__":
    app.run(debug=True, port=settings.PORT, host=settings.PORT)