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
        "views/view_helpdesk_ticket_form_inherit_purchase.xml",
        # "views/helpdesk_purchase_line_views.xml",
        # "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
