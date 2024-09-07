# -*- coding: utf-8 -*-

import base64
from odoo import http
from odoo.http import request


class home_controller(http.Controller):
    """Controller for taking Home"""

    @http.route('/mis_home', type='http', auth='public', website=True)
    def mis_home_temp(self):
        """To redirect to contact page."""
        return request.render('mis_website.mis_home_page')
