from flask import Flask, redirect, url_for

app = Flask(__name__)
app.secret_key = 'adfadfdafaesfeatrasffdafadfad'
app.config.from_pyfile('config.cfg')

from route import app_route
from route_auth import app_route_auth

app.register_blueprint(app_route)
app.register_blueprint(app_route_auth)

# faviconがないエラーを解消するためのルート
@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if __name__ == '__main__':
  app.run(host='127.0.0.1',port=5000)

