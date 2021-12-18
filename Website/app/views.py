#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:51:17 2021

@author: sc20a2bm
"""

from flask import render_template, flash, request, redirect
from app import app, db, models
from .models import User, AccountItem, Coach
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import logging

logging.basicConfig(filename='log.log',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html', user=current_user)


@app.route('/login', methods=['GET','POST'])
def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
    
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    logging.info('Account logged in: {} '.format(current_user.username))

                    return redirect('/')
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Account does not exist.', category='error')

        return render_template("login.html", user=current_user)

    
@app.route('/logout')
@login_required
def logout():
        logging.info('User logged out: {} '.format(current_user.username))
        logout_user()
        return redirect('/login')
    
@app.route('/additem', methods=['GET','POST'])
@login_required
def additem():
    if(request.method == 'POST'):
        role = request.form.get('role')
        rank = request.form.get('rank')
        price = request.form.get('price')
        coach = request.form.get('coach')
        coach_ = User.query.filter_by(username=coach).first()
        
        try:
            f = float(price)
            if(float(price) > 0):
               if coach_:
                   new_coach=Coach(rank=rank,role=role,price=f,Coach=coach_.id)
                   db.session.add(new_coach)
                   db.session.commit()
               else:
                   flash('Coach not found', category='error')
            else:
                flash('Invalid Price', category='error')
        except Exception:
            flash('Invalid Price', category='error')

    return render_template("additem.html", user=current_user)

@app.route('/additem2', methods=['GET','POST'])
@login_required
def additem2():
    if(request.method == 'POST'):
        price = request.form.get('price')
        seller = request.form.get('seller')
        seller_ = User.query.filter_by(username=seller).first()
        description = request.form.get('desc')
        server = request.form.get('server')
        be = request.form.get('be')
        
        try:
            f = float(price)
            b = float(be)
            if(float(price) > 0 and float(be) > 0):
               if seller_:
                       new_item=AccountItem(price=f,blue_essence=b,server=server, description = description,seller=seller_.id)
                       db.session.add(new_item)
                       db.session.commit()
               else:
                   flash('Seller not found', category='error')
            else:
                flash('Invalid Price/Blue Essense', category='error')
        except Exception:
            flash('@Invalid Price/Blue Essense', category='error')

    return render_template("additem2.html", user=current_user)
    
@app.route('/signup', methods=['GET','POST'])
def signup():
    if(request.method == 'POST'):
        email = request.form.get('email')
        user_Name = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        user1 = User.query.filter_by(username=user_Name).first()
        if user:
            flash('Email already exists.', category='error')
        if user1:
            flash('Username already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(user_Name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=user_Name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            logging.info('Account created: {} '.format(current_user.username))
            return redirect('/')

    return render_template("sign_up.html", user=current_user)

@app.route('/accounts', methods=['GET','POST'])
def accounts():
    return render_template('accounts.html', user=current_user, accounts = models.AccountItem.query.all())

@app.route('/coaching', methods=['GET','POST'])
def coaching():
    return render_template('coaching.html', user=current_user, coaches = models.Coach.query.all())

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html', user=current_user)

@app.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/changepassword', methods=['GET','POST'])
@login_required
def changepassword():
    if(request.method == 'POST'):

        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        password3 = request.form.get('password3')
        user = current_user
                
        if(check_password_hash(user.password, password1)):
            if(len(password2) > 6):
                if(password2 == password3):
                    
                    user.password = generate_password_hash(password2, method='sha256')
                    db.session.commit()
                    flash('Password Changed!', category='success')
                    logging.info('Change password: {} '.format(user.username))
    
                else:
                    flash('New Passwords do not match', category='error')
                    logging.warning('New Passwords do not match: {} '.format(user.username))
            else:
                flash('New Password is too short', category='error')
                logging.warning('New Password is too short: {} '.format(user.username))               
        else:
            flash('Old Password does not match', category='error')
            logging.warning('Old Password does not match: {} '.format(user.username))



    return render_template('changepassword.html', user=current_user)