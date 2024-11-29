# -*- coding: utf-8 -*-
{
    'name': 'Custom_estancias',
    'version': '17.0.1.0',
    'summary': """ Custom_estancias Summary """,
    'author': 'Pedro Mayor',
    'website': '',
    'category': '',
    'depends': ['base', 'res.partner', 'helpdesk'],
    "data": [
        "views/sedes_estancias_views.xml",
        "security/ir.model.access.csv",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
