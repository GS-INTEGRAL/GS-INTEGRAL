{
    "name": "Custom Helpdesk Extension",
    "version": "1.0",
    "summary": "Extensión del módulo de Helpdesk con campos personalizados",
    "author": "Pedro Mayor",
    "category": "Helpdesk",
    "license": "LGPL-3",
    "depends": [
        "web",
        "helpdesk",
        "website_helpdesk",
        "base",
        "website",
        "custom_auth_sing_in",
    ],
    "data": [
        "static/assets.xml",
        "views/helpdesk_ticket_views.xml",
        "views/website_helpdesk_ticket_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "custom_helpdesk/static/src/js/dynamic_helpdesk.js",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
