from odoo import models, fields, api


class Obra(models.Model):
    _name = "obra"
    _description = "Obra"

    name = fields.Char(string="Nombre de la Obra", required=True)
    estancias_ids = fields.One2many("estancias.capitulo", 'obra_id', string="Estancias")
    partner_ids = fields.One2many('res.partner', 'obra_id', string="Partners")

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        # Esto mejorará la búsqueda en campos relacionales
        args = args or []
        domain = [('name', operator, name)]
        return self.search(domain + args, limit=limit).name_get()