# -*- coding: utf-8 -*-
{
    "name": "Custom_order_purchase",
    "version": "17.0.1.0.0",
    "summary": """ Custom_order_purchase Summary """,
    "author": "Pedro Mayor",
    "website": "",
    "category": "Implements",
    "depends": [
        "helpdesk",
        "purchase",
    ],
    "data": [
        'wizard/purchase_order_confirmation_wizard_view.xml',
        "views/view_helpdesk_ticket_form_inherit_purchase.xml",
        "views/view_purchase_order_form.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
