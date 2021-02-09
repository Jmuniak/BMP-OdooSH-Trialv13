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
        
        # load the security XML file first. Odoo loads the files in order.
        'security/academy_security.xml',
        # if we define any GROUPS in the XML file and we will need to load them before the access rights in the CSV
        # this can cause an error if not loaded in the right order.
        'security/ir.model.access.csv',
        
        'views/academy_menuitems.xml',
        #'views/course_views.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
}