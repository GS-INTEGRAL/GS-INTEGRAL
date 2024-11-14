from odoo import models, fields, api


class Estancia(models.Model):
    _name = "estancias.capitulo"
    _description = "Estancias y Planos"

    name = fields.Char(string="Estancia", required=True)
    plano = fields.Binary(string="Plano", attachment=True)
    obra_id = fields.Many2one('obra', string="Obra")  
    partner_ids = fields.Many2many('res.partner', string="Asignados")

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        # Esto mejorará la búsqueda en campos relacionales
        args = args or []
        domain = [('name', operator, name)]
        return self.search(domain + args, limit=limit).name_get()
