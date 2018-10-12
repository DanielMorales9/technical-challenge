from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys, os

from solver.solver import solver
from helpers.middleware import setup_metrics
from flask import Flask
import json
import prometheus_client
from flask import Response, request

env2config = dict({
    'dev': 'default-settings.DevelopmentConfig',
    'prod': 'default-settings.ProductionConfig',
    'test': 'default-settings.TestingConfig'
})

app = Flask(__name__)
setup_metrics(app)
app.config.from_object(env2config.get(os.getenv('ENV', 'dev')))
app.config.from_envvar("SERVER_NAME", silent=True)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')


# The root endpoint returns the app value. Some percentage of the time
# (given by app.config['failure_rate']) calls to this endpoint will cause the
# app to crash (exits non-zero).
@app.route('/v1/')
def index():
    input_val = json.loads(request.args.get("input"))
    result = solver(input_val)
    return result


@app.route('/metrics/')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


# To help with testing this endpoint will cause the app to crash
# every time it is called
@app.route('/crash')
def crash():
    request.environ.get('werkzeug.server.shutdown')()
    app.config.update({'crashed': True})
    return "{}"


if __name__ == '__main__':
    app.run()

    if app.config['crashed']:
        print('app crashed, exiting non-zero')
        sys.exit(1)
