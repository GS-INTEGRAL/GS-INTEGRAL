from odoo import models, fields

class ResPartnerObraSecundaria(models.Model):
    _inherit = 'res.partner.obra_secundaria'

    is_obra_secundaria = fields.Boolean(default=True)
