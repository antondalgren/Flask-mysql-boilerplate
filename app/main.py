__author__ = 'antda685'

import json
from flask import Flask
import queries as query

app = Flask(__name__)
app.config.update(dict(
    DATABASE="Database",
    USERNAME="username",
    HOST="host",
    PASSWORD="password"
))


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/users")
def users():
    return json.dumps({'success': 'success', 'results': query.get_users()})


if __name__ == "__main__":
    app.run()
