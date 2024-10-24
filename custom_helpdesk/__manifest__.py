{
    'name': 'Custom Helpdesk Extension',
    'version': '1.0',
    'summary': 'Extensión del módulo de Helpdesk con campos personalizados',
    'author': 'Pedro Mayor',
    'category': 'Helpdesk',
    'license': 'LGPL-3',
    'depends': ['helpdesk', 'website_helpdesk'],
    'depends': ['helpdesk', 'website_helpdesk'],
    'data': [
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

