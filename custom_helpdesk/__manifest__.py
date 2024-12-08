{
    "name": "Custom Helpdesk Extension",
    "version": "17.0.1.0",
    "summary": "Extensión del módulo de Helpdesk con campos personalizados",
    "author": "Pedro Mayor",
    "category": "Helpdesk",
    "license": "LGPL-3",
    "depends": [
        "helpdesk",
        "website_helpdesk",
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/helpdesk_permission.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "assets":{
        "web.assets_frontend": [
            'custom_helpdesk/static/src/js/form.js',
            'custom_helpdesk/static/src/xml/website_helpdesk_ticket_views.xml',
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
