from flask import Flask, redirect, url_for

app = Flask(__name__)

from route import app_route

app.register_blueprint(app_route)

# faviconがないエラーを解消するためのルート
@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if __name__ == '__main__':
  app.run(host='127.0.0.1',port=5000)

