# -*- coding: utf-8 -*-
import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class Sede(models.Model):
    _name = "sedes"
    _description = "Sedes/Obras"

    obra_secundaria = fields.Char(string="Obra/sede")


class Estancia(models.Model):
    _name = "estancias"
    _description = "Estancias"

    estancia_id = fields.Char(string="Estancia")
 

