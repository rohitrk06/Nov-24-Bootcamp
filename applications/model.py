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
    # user.customer_details.name


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

# class StoreManager(User):
#     store_crediantials = db.Column(db.String(100), nullable=False)


#More Models to be added

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False, unique=True)

    # products = db.relationship("Products")
    products = db.relationship("Products", backref="category")

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    cost_price = db.Column(db.Float, nullable=False)

    mfg_date = db.Column(db.Date, nullable=False)
    exp_date = db.Column(db.Date, nullable=False)

    img_url = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    # category = db.relationship("Categories", uselist=False)


