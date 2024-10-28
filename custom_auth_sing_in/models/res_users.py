from odoo import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    sede = fields.Char("Sede")
    lugar = fields.Char("Lugar")
