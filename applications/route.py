from flask import render_template, request, url_for, session, redirect, flash
from main import app
from applications.database import db
from applications.model import *
from datetime import datetime
import os


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
    

@app.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == 'GET':
        all_categories = Categories.query.all()
        # all_categories[0].category_name
        return render_template('addProduct.html',categories = all_categories )
    
    if request.method =='POST':
        product_name = request.form.get('product_name')
        description = request.form.get('description')
        price = request.form.get('selling_price')
        cost_price = request.form.get('cost_price')
        mfg_date = request.form.get('mfg_date')
        exp_date = request.form.get('expiry_date')
        # img_url = request.form.get('product_image')
        category_id = request.form.get('category')
        product_image = request.files.get('product_image')
        

        print(product_name,description,price,cost_price,mfg_date,exp_date,category_id,product_image)
        #data validation
        #define various data validation you want for your application -- can be done
        if not product_name or not description or not price or not cost_price or not mfg_date or not exp_date or not category_id:
            #flash message
            print("checkpoint 1")
            return redirect(url_for('add_product'))

        # '2024-11-18' --> %Y-%m-%d
        mfg_date = datetime.strptime(mfg_date,"%Y-%m-%d")
        exp_date = datetime.strptime(exp_date,"%Y-%m-%d")
        # "18 Nov,2024"

        if exp_date<=mfg_date:
            #flash message
            print("checkpoint 2")

            return redirect(url_for('add_product'))
        
        if not Categories.query.get(category_id):
            #flash message
            print("checkpoint 3")

            return redirect(url_for('add_product'))
        
        img_url = ''
        if product_image:
                filename = product_image.filename
                path = 'product_image/' + filename
                relative_path = os.path.join('static',path)
                product_image.save(relative_path)
                img_url = path
        # url_for('static',filename = img_url)
        product = Products(product_name = product_name,
                           description = description,
                           price = price,
                           cost_price = cost_price,
                           mfg_date = mfg_date,
                           exp_date = exp_date,
                           img_url = img_url,
                           category_id = category_id
                           )
        db.session.add(product)
        db.session.commit()

        #flash message  
        flash("Product Added Successfully")
        return redirect(url_for('index'))

    



