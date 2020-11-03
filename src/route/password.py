from flask import Flask, render_template, request, Blueprint

password = Blueprint('password', __name__, url_prefix='/password')

@password.route('/index')
def index():
  return render_template('password.html', title='PASSWORD')