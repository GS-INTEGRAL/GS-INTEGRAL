from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    sede = fields.Char(string="Sede")
    lugar = fields.Char(string="Lugar")
