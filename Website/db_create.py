#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:36:01 2021

@author: sc20a2bm
"""

from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path

db.create_all()