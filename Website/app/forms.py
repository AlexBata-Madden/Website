#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:24:39 2021

@author: sc20a2bm
"""

from flask_wtf import Form
from wtforms import IntegerField, TextField, TextAreaField
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired, Regexp, Length

class CalculatorForm(Form):
    number1 = IntegerField('number1', validators=[DataRequired()])
    number2 = IntegerField('number2', validators=[DataRequired()])
    
class CreateAssessment(Form):
    title = TextField('title', validators=[DataRequired(), Length(max=100)])
    m1 = "Must be in the format 4 Letters 4 Numbers"
    m2 = "Module code is not the right length"
    module_code =  TextField('module_code', validators=[DataRequired(), 
                                                        Regexp('[A-Z]{4}[0-9]{4}',
                                                               message = m1), Length(min=8,max=8,message=m2)])
    deadline = DateField('deadline', format="%Y-%m-%d",validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired(), Length(max = 500)])