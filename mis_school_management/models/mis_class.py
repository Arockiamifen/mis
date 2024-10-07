from odoo import models, fields

class ClassMaster(models.Model):
    _name = 'mis.class'
    _description = 'MIS Class Master'

    name = fields.Char(string='Class Name', required=True)
    class_teacher_id = fields.Many2one('mis.teacher', string='Class Teacher', required=True)
    student_ids = fields.One2many('mis.student', 'class_id', string='Students')
    capacity = fields.Integer(string='Class Capacity')
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('unique_class_name', 'unique(name)', 'Name should be unique per Class!'),
    ]



class ClassMasterConfig(models.Model):
    _name = 'class.master.config'
    _description = 'Class Master Config'



    name = fields.Char(string='Class Name', required=True)
    date = fields.Datetime('Date')

    _sql_constraints = [
        ('unique_class_name', 'unique(name)', 'Name should be unique per Class!'),
    ]


