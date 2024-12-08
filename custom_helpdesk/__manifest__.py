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
        "security/helpdesk_permission.xml",
        "views/helpdesk_ticket_views.xml",
        "views/website_helpdesk_ticket_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
