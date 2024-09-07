# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from random import randint


class ProgramEvents(models.Model):
    _name = 'program.events'

    name = fields.Char('Name', required=True)
    date = fields.Datetime('Date', default=lambda self: fields.Datetime.now())

class ProgramEventsGallery(models.Model):
    _name = 'program.gallery'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', readonly=True, default='New')
    date = fields.Date('Date',default=lambda self: fields.Datetime.now(), readonly=True)
    user_id = fields.Many2one('res.users', 'Created By', default=lambda self: self.env.user, readonly=True)
    event_id = fields.Many2one('program.events', 'Event')
    photo_ids = fields.One2many('program.gallery.photo','gallery_id', 'Photos')
    remarks = fields.Char('Remarks')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'name' not in vals or vals['name'] == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('program.gallery') or _('New')
        return super().create(vals_list)


class ProgramEventsGallery(models.Model):
    _name = 'program.gallery.photo'

    gallery_id = fields.Many2one('program.gallery','Photo Gallery')
    name = fields.Char('Name')
    tag_ids = fields.Many2many('photo.tag', 'Tags')
    place = fields.Char('Place')
    date = fields.Date(related='gallery_id.date', string='Date')
    event_id = fields.Many2one(related='gallery_id.event_id', string='Event')
    photo = fields.Image(string="Image", max_width=80, max_height=50)
    file_name = fields.Char('File Name')


class PhotoTag(models.Model):
    _name = "photo.tag"
    _description = "Photo Tag"

    def _default_color(self):
        return randint(1, 11)

    name = fields.Char("Name", required=True, translate=True)
    color = fields.Integer(
        string='Color Index', default=lambda self: self._default_color(),
        help='Tag color. No color means no display in kanban or front-end, to distinguish internal tags from public categorization tags.')







