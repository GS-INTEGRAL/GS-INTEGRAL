# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class Sede(models.Model):
    _name = "sedes"
    _description = "Sedes/Obras"

    name = fields.Char("Nombre de la Sede/Obra", required=True)
    estancias_ids = fields.One2many("estancias", "sede_id", string="Estancias")


class Estancia(models.Model):
    _name = "estancias"
    _description = "Estancias"

    name = fields.Char("Nombre de la Estancia", required=True)
    sede_id = fields.Many2one("sedes", string="Sede/Obra")


class HelpdeskTicketInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    estancia_id = fields.Many2one('estancias', string='Estancia')
    sede_id = fields.Many2one(
        'sedes', string='Sede', 
        compute='_compute_sede', store=True, readonly=False
    )

    @api.depends('estancia_id')
    def _compute_sede(self):
        for ticket in self:
            ticket.sede_id = ticket.estancia_id.sede_id if ticket.estancia_id else False


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    sede_ids = fields.One2many('sedes', 'partner_id', string='Sedes')
