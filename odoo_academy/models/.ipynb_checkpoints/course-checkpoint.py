# _*_ coding: utf-8 _*_

from odoo import models, fields, api

class Course(models.Model):
    # use the name you want the model to be: Course in this case.
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    # next we will have a description field so it can be longer
    description = fields.Text(string='Description')
    
    # selection field. Level field: the level of the current course
    level = fields.Selection(string='Level',
                            selection=[('beginner', 'Beginner'),
                                      ('intermediate', 'Intermediate'),
                                      ('advanced', 'Advanced')],
                            copy=False)
    
    # using a reserved field namne
    active = fields.Boolean(string='Active', default=True)