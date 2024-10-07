# -*- coding: utf-8 -*-

from odoo import fields, models


class EducationClass(models.Model):
    """For managing classes"""
    _name = 'education.class'
    _description = "Standard"

    name = fields.Char(string='Name', required=True,
                       help="Enter the Name of the Class")
    syllabus_ids = fields.One2many('education.syllabus',
                                   'class_id',
                                   string="Syllabus",
                                   help="Syllabus of the class")
    division_ids = fields.One2many('education.division',
                                   'class_id',
                                   string="Division",
                                   help="Divisions of class")
