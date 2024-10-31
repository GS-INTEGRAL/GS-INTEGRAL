{
    'name': 'Website Helpdesk Extended',
    'version': '1.0',
    'summary': 'Extends Website Helpdesk with additional fields',
    'description': """
        This module extends the Website Helpdesk functionality by adding
        a 'Sede' field to the ticket submission form and ticket model.
    """,
    'category': 'Services/Helpdesk',
    'author': 'pedro mayor',
    'website': 'https://www.gs-integral-murcia.com',
    'license': 'LGPL-3',
    'depends': ['website_helpdesk'],
    'data': [
        'views/helpdesk_templates.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
