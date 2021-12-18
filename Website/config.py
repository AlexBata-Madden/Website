#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:23:38 2021

@author: sc20a2bm
"""
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = "no-one-will-guess-this"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
