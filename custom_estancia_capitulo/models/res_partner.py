class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    obra_id = fields.Many2one('obra', string="Obra")
