# -*- coding: utf-8 -*-

from odoo import models, fiels, api

class Course(models.Model):
    # use the name you want the model to be: Course in this case.
    _name = 'academy.course'
    _description = 'Course Info'