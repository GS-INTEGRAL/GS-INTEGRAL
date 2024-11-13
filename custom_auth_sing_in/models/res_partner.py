from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    obra_id = fields.Many2one('obra', string="Sede/Obra")  # Cambia 'obra' por el nombre del modelo correspondiente si existe
    estancia_id = fields.Many2one('estancias.capitulo', string="Estancia/Capitulo")
