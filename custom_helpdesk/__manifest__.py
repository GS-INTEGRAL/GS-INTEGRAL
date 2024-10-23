{
    'name': 'Custom Helpdesk Extension',
    'version': '1.0',
    'summary': 'Extensión del módulo de Helpdesk con campos personalizados',
    'author': 'Pedro Mayor',
    'category': 'Helpdesk',
    'license': 'LGPL-3',
    'depends': ['helpdesk', 'website_helpdesk'],
    'data': [
        'views/helpdesk_ticket_views.xml',
        'views/website_helpdesk_team_form_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

