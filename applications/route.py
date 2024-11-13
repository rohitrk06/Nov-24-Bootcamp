from flask import render_template, request, url_for, session, redirect
from main import app
from applications.database import db
from applications.model import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_category', methods=['GET','POST'])
def add_category():
    if request.method == 'GET':
        
        if session['role'] != 'admin':
            #flash message
            return redirect(url_for('index'))
        
        return render_template('addcategory.html')
    
    if request.method == 'POST':

        category_name = request.form.get('category_name')

        if not category_name:
            #flash message 
            return redirect(url_for('add_category'))
        
        if Categories.query.filter_by(category_name = category_name).first():
            #flash message
            return redirect(url_for('add_category'))
        
        if session['role'] != 'admin':
            #flash message
            return redirect(url_for('index'))

        category = Categories(category_name = category_name)
        db.session.add(category)
        db.session.commit()
        #flash message
        return redirect(url_for('index'))
    


    



