from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    sede = fields.Char(
        string="Sede", help="Centro en general donde se ha producido la incidencia"
    )
    lugar = fields.Char(
        string="Lugar",
        help="Sitio exacto dentro de la sede donde se ha producido la incidencia",
    )
