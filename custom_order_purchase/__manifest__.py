# -*- coding: utf-8 -*-
{
    'name': 'Custom_order_purchase',
    'version': '17.0.1.0.0',
    'summary': """ Custom_order_purchase Summary """,
    'author': 'Pedro Mayor',
    'website': '',
    'category': 'Implements',
    'depends': ['base', 'web'],
    "data": [
        "security/ir.model.access.csv",
        "views/employee_order_purchase_views.xml"
    ],
    'assets': {
              'web.assets_backend': [
                  'custom_order_purchase/static/src/**/*'
              ],
          },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
