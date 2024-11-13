from flask import render_template, request, url_for, session, redirect
from main import app
from applications.database import db
from applications.model import *


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        # request.form.get('email')
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            # flash error messages
            return render_template('login.html')
        
        user = User.query.filter_by(email_id = email).first()   
        if not user:
            # flash error messages
            return render_template('login.html')
        
        if user.password != password:
            # flash error messages
            return render_template('login.html')
        
        session['user_id'] = user.user_id
        session['email_id'] = user.email_id
        session['role'] = user.roles[0].role_name

        return render_template('index.html')
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('email_id', None)
    session.pop('role', None)
    return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        address = request.form.get('address')
        role = request.form.get('role')

        #data validation

        if not email or not password or not confirm_password or not address or not role:
            # flash error messages
            return redirect(url_for('register'))
        
        if password != confirm_password:
            # flash error messages
            return redirect(url_for('register'))
        
        user = User.query.filter_by(email_id = email).first()
        if user:
            # flash error messages
            return redirect(url_for('register'))
        
        new_user_role = Role.query.filter_by(role_name = role).first()
        if not new_user_role:
            # flash error messages
            return redirect(url_for('register'))
        
        new_user = User(
            email_id = email,
            password = password,
            address = address,
            roles = [new_user_role]
        )

        db.session.add(new_user)
        db.session.commit()

        if new_user.roles[0].role_name == 'customer':
            return redirect(url_for('complete_profile', id = new_user.user_id))

        #flash success messages
        return redirect(url_for('login'))
        
# /compelte_profile/5

@app.route('/complete_profile/<int:id>', methods=['GET','POST'])
def complete_profile(id):
    if request.method == 'GET':
        user = User.query.get(id)
        if not user:
            # flash error messages
            return redirect(url_for('index'))
        
        return render_template('customer_registration_details.html',user_id = user.user_id)
    
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('mob')

        user = User.query.get(id)
        if not user:
            # flash error messages
            return redirect(url_for('index'))
        
        customer = Customer(
            user_id = user.user_id,
            name = name,
            phone = phone
        )

        db.session.add(customer)
        db.session.commit()

        #flash success messages
        return redirect(url_for('login'))



        

