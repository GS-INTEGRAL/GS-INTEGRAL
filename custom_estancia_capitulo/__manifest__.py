{
    "name": "Custom estancia capitulo",
    "version": "17.0",
    "summary": "Custom estancia capitulo",
    "description": "Modulo para tener un archivo de las estancias",
    "category": "Construction",
    "author": "Pedo Mayor",
    "license": "LGPL-3",
    "depends": [
        "base",
        "website_helpdesk",
        "helpdesk",
        "custom_auth_sing_in",
      ],
    "data": [
        "security/ir.model.access.csv",
        "views/estancia_view.xml",
    ],
    "images": [
        "static/description/icon_estancias_capitulo.png",
    ],
    "installable": True,
    "application": True,
}
