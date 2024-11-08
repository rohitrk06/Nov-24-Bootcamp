from applications.database import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    # role = db.Column(db.String(100), unique = False)

    roles = db.relationship("Role", secondary="user_role")
    #[<role 1> , <role 2>]
    customer_details = db.relationship("Customer",uselist=False)
    # <customer 1>


    # Optional
    # def __repr__(self):
    #     return f"User('{self.email_id}')"

class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(100), nullable=False)

# user_role
class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"),unique=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=True)
    payment_details = db.Column(db.String(100), nullable=True)

# class StoreManager(User):
#     store_crediantials = db.Column(db.String(100), nullable=False)


