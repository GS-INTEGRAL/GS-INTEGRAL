from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    sede = fields.Selection([
        ('sede1', 'Sede 1'),
        ('sede2', 'Sede 2'),
        ('sede3', 'Sede 3'),
    ], string='Sede')
