from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    obra_id = fields.Selection(
        [
            ("lavaqua", "Lavaqua"),
            ("legal fincas", "Legal Fincas"),
            ("clientes varios", "Clientes Varios"),
            ("maristas", "Maristas"),
        ],
        string="Cliente",
    )
    obra_secundaria = fields.Char(string="Obra/sede")
    estancia_id = fields.Char(string="Estancia/Capítulo")


class PartnerEstancia(models.Model):
    _name = "res.partner.estancia_id"
    _order = "name"
    _description = "Partner Estancia"

    name = fields.Char(string="Estancia/Capítulo", required=True, translate=True)


class PartnerObraSecundaria(models.Model):
    _name = "res.partner.obra_secundaria"
    _order = "name"
    _description = "Partner Obra Secundaria"

    name = fields.Char(string="Obra/sede", required=True, translate=True)
