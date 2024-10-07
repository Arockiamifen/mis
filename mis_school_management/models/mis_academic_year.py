# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import timedelta


class MisAcademicYear(models.Model):
    _name = 'mis.academic.year'
    _description = "Academic Year"

    name = fields.Char('Name', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    create_boolean = fields.Boolean()


