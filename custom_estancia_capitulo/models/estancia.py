from odoo import models, fields


class Estancia(models.Model):
    _name = "estancias.capitulo"
    _description = "Estancias y Planos"

    estancia = fields.Char(string="Estancia", required=True)
    plano = fields.Binary(string="Plano", attachment=True)
    obra_id = fields.Many2one('obra', string="Obra")  
    partner_ids = fields.Many2many('res.partner', string="Asignados")