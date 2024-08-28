# -*- coding: utf-8 -*-

from odoo import api, fields, models


class UniversitySemester(models.Model):
    """Used to manage the semester of department"""
    _name = 'university.semester'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "University Semester"

    # @api.model
    # def create(self, vals):
    #     """ This method overrides the create method to generate the name for
    #         the semester based on the department code and semester number.
    #
    #         :param vals (dict): Dictionary containing the field values for the
    #                             new university semester record.
    #         :returns class:`~university.semester`: The created university
    #                         semester record."""
    #     department_id = self.env['university.department'].browse(
    #         vals['department_id'])
    #     name = str(department_id.code) + '/Sem ' + str(vals['semester_no'])
    #     vals['name'] = name
    #     return super(UniversitySemester, self).create(vals)

    name = fields.Char(string="Name", help="Name of the semester",
                       readonly=True)
    semester_no = fields.Integer(string="Semester", help="Semester number",
                                 required=True)
    department_id = fields.Many2one('university.department',
                                    string="Department",
                                    required=True,
                                    help="In which department the semester "
                                         "belongs to")
    syllabus_ids = fields.One2many('university.syllabus',
                                   'semester_id',
                                   help="Syllabus of semester",
                                   string="Syllabus")
