from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sede = fields.Char("Sede")
    lugar = fields.Char("Lugar")
