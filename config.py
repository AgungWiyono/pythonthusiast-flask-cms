class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://myuser:mypassword@postgres:5432/flask01'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='guess that'
