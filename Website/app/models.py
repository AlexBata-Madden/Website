#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:50:38 2021

@author: sc20a2bm
"""
from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Coach(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     rank = db.Column(db.String(20))
     role = db.Column(db.String(20))
     price = db.Column(db.Float())
     Coach = db.Column(db.Integer, db.ForeignKey('user.id'))  
    
class AccountItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float())
    blue_essence = db.Column(db.Float())
    server = db.Column(db.String(20))
    description = db.Column(db.String(200))
    seller = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(60))
    username = db.Column(db.String(200), unique=True)
    accounts = db.relationship('AccountItem', backref='owned_user', lazy=True)
    coaches = db.relationship('Coach', backref='owned_coach', lazy=True)