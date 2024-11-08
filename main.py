from flask import Flask
from applications.database import db
from applications.config import Config
from applications.model import *

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # app.app_context().push()

    # more things will come here

    return app

app = create_app()  


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)


