# -*- coding: utf-8 -*-

import base64
from odoo import http
from odoo.http import request


class program_events_controller(http.Controller):
    """Controller for taking Prospectus"""

    @http.route('/program_events_gallery', type='http', auth='public', website=True)
    def program_events_gallery_cont(self):
        """To redirect to contact page."""

        vals = {
            'photos': request.env['program.gallery.photo'].sudo().search([]),
            'events': request.env['program.events'].sudo().search([]),
        }
        print('LODFFFFFFFFFFFFFFFFF',vals)
        return request.render('mis_website.program_events_gallery', vals)
