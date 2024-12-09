from odoo import models, fields

class ResPartnerEstancia(models.Model):
    _inherit = 'res.partner.estancia_id'

    is_estancia = fields.Boolean(default=True)
