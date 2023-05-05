# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import logging

from odoo import http


from odoo.http import request

_logger = logging.getLogger(__name__)


class About(http.Controller):
    @http.route('/about', website=True, type='http', auth='public', csrf=False)
    def about_page(self):
        return request.render('theme_levelup.about_page')

    @http.route('/portfolio', website=True, type='http', auth='public', csrf=False)
    def portfolio_page(self):
        return request.render('theme_levelup.portfolio_page')

    @http.route('/team', website=True, type='http', auth='public', csrf=False)
    def team_page(self):
        return request.render('theme_levelup.team_page')

    @http.route('/service', website=True, type='http', auth='public', csrf=False)
    def service_page(self):
        return request.render('theme_levelup.service_page')

    @http.route('/blog_snippet', auth="public", type='json', website=True)
    def latest_blog(self):
        return request.env['blog.post'].sudo().search_read([],limit=3)

