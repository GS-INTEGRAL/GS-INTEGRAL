{
    'name': 'Custom Helpdesk View',
    'version': '1.0',
    'category': 'Helpdesk',
    'summary': 'Personalización de formulario Helpdesk para clientes.',
    'description': """
        Este módulo contiene campos específicos para clientes.
    """,
    'author': 'Your Name',
    'depends': ['helpdesk'],
    'data': [
        'views/helpdesk_ticket_view_inherit.xml',
    ],
    'installable': True,
    'application': False,
}
