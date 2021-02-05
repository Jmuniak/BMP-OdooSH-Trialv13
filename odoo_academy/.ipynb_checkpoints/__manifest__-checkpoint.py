# _*_ coding: utf-8 _*_

{
    'name': 'Odoo Academy',
    'summary': """Academy to manage Training""",
    'description': """
        Academy to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Jeremy M',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'views/course_views.xml',
        'views/academy_menuitems.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}