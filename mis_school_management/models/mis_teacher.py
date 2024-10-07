# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MisTeacher(models.Model):
    _name = "mis.teacher"
    _description = "MIS Teacher"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one('res.partner', 'Partner',
                                 required=True, ondelete="cascade")
    first_name = fields.Char('First Name', translate=True, required=True)
    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128, required=True)
    birth_date = fields.Date('Birth Date', required=True)
    blood_group = fields.Selection([
        ('A+', 'A+ve'),
        ('B+', 'B+ve'),
        ('O+', 'O+ve'),
        ('AB+', 'AB+ve'),
        ('A-', 'A-ve'),
        ('B-', 'B-ve'),
        ('O-', 'O-ve'),
        ('AB-', 'AB-ve')
    ], string='Blood Group')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], 'Gender', required=True)
    nationality = fields.Many2one('res.country', 'Nationality')
    emergency_contact = fields.Many2one(
        'res.partner', 'Emergency Contact')
    visa_info = fields.Char('Visa Info', size=64)
    id_number = fields.Char('ID Card Number', size=64)
    login = fields.Char(
        'Login', related='partner_id.user_id.login', readonly=True)
    last_login = fields.Datetime('Latest Connection', readonly=True,
                                 related='partner_id.user_id.login_date')
    # faculty_subject_ids = fields.Many2many('mis.subject', string='Subject(s)',
    #                                        tracking=True)
    emp_id = fields.Many2one('hr.employee', 'HR Employee')
    active = fields.Boolean(default=True)

    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))

    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name(self):
        if not self.middle_name:
            self.name = str(self.first_name) + " " + str(
                self.last_name)
        else:
            self.name = str(self.first_name) + " " + str(
                self.middle_name) + " " + str(self.last_name)

    # def create_employee(self):
    #     for record in self:
    #         vals = {
    #             'name': record.name,
    #             'country_id': record.nationality.id,
    #             'gender': record.gender,
    #             'private_state_id': record.partner_id.id
    #         }
    #         emp_id = self.env['hr.employee'].create(vals)
    #         record.write({'emp_id': emp_id.id})
    #         record.partner_id.write({'partner_share': True, 'employee': True})
