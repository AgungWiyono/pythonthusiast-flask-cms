from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db=SQLAlchemy(app)

    @app.route('/')
    def index():
        return 'Halo Flask, hot reload'

    @app.route('/about')
    def about():
        return 'About me'

    @app.route('/dbtest')
    def dbtest():
        import psycopg2

        con = psycopg2.connect('dbname=flask01 user=myuser password=mypassword\
                                host=postgres')
        cur = con.cursor()

        cur.execute('select * from page;')
        id, title = cur.fetchone()
        con.close()
        return 'Ouput table page :{} - {} '.format(id, title)

    return app
