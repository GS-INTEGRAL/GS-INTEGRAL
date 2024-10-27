{
    'name': 'Custom auth sing in',
    'version': '1.0',
    'summary': 'Custom auth sing in',
    'description': 'Campos en el sign in',
    'category':  'Website',
    'author': 'Pedo Mayor',
    'license': 'LGPL-3',
    'depends': ['auth_signup', 'website_helpdesk'],
    'data': [
            'views/auth_signup_login_inherit.xml',
            ],
        
    'installable': True,
    'application': False,
    'auto_install': False
}
