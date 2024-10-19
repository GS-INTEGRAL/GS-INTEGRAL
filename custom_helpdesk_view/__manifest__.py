{
    'name': 'Custom Helpdesk View',
    'version': '1.0',
    'category': 'Helpdesk',
    'summary': 'Personalización de formulario Helpdesk para clientes.',
    'description': """
        Este módulo contiene campos específicos para clientes.
    """,
    'author': 'GS-INTEGRAL',  # Cambia esto por tu nombre real o el de tu empresa
    'depends': ['helpdesk'],
    'data': [
        'views/helpdesk_ticket_view_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,  # Cambia a True si deseas que se instale automáticamente cuando se instala el módulo dependiente
}

