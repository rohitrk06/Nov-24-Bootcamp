class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'secret_key'
    # SECURITY_SALT = 'security_salt'