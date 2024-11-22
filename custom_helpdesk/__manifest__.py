{
    "name": "Custom Helpdesk Extension",
    "version": "17.0.0",
    "summary": "Extensión del módulo de Helpdesk con campos personalizados",
    "author": "Pedro Mayor",
    "category": "Helpdesk",
    "license": "LGPL-3",
    "depends": [
        "helpdesk",
        "website_helpdesk",
        "base",
        "website",
        "custom_auth_sing_in",
    ],
    "data": [
        "views/helpdesk_ticket_views.xml",
        "views/website_helpdesk_ticket_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
