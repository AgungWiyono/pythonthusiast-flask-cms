from flask import render_template, Blueprint

from app import db

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('hello.html', title='Hello page')

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')

@bp.route('/dbtest', methods=['GET'])
def dbtest():
    return 'This page is still in development'



