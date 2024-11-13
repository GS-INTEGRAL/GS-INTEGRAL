from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    obra_id = fields.Char(string="Sede/Obra")
    estancia_id = fields.Char(string="Estancia/Capitulo")
