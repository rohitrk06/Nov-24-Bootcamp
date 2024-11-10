from flask import Flask, render_template
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
        # more things will come here

        #Role.query.all()
        #Role.query.filter_by(role_name='admin').all()

        admin_role = Role.query.filter_by(role_name='admin').first()
        if not admin_role:
            admin_role = Role(role_name='admin')
            db.session.add(admin_role)

        store_manager_role = Role.query.filter_by(role_name='store_manager').first()
        if not store_manager_role:
            store_manager_role = Role(role_name='store_manager')
            db.session.add(store_manager_role)

        customer_role = Role.query.filter_by(role_name='customer').first()
        if not customer_role:
            customer_role = Role(role_name='customer')
            db.session.add(customer_role)

        # print(type(admin_role))  # <class 'applications.model.Role'>

        admin = User.query.filter_by(email_id = 'admin@gmail.com').first()
        if not admin:
            admin = User(
                email_id = 'admin@gmail.com',
                password = 'admin',
                address = 'admin address',
                roles = [admin_role],
                #assumne we object of class Customer
                # customer_details = [Customer(name='admin', phone='1234567890', payment_details='payment details')] not the right way
                # correct way is below
                # customer_details = Customer(name='admin', phone='1234567890', payment_details='payment details')
            )
            db.session.add(admin)
        
        db.session.commit()

    # app.app_context().push()

    return app

app = create_app()  


from applications.routes import *


if __name__ == '__main__':
    app.run(debug=True)


