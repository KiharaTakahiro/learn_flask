from flask import Flask, redirect, url_for

app = Flask(__name__)

from route.menu import menu
from route.login import login
from route.password import password
from route.user_master import user_master

app.register_blueprint(menu)
app.register_blueprint(login)
app.register_blueprint(password)
app.register_blueprint(user_master)

# faviconがないエラーを解消するためのルート
@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if __name__ == '__main__':
  app.run(host='127.0.0.1',port=5000)

