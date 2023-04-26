# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
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

{
    'name': 'Theme Levelup',
    'description': 'The perfect website theme for your growing business',
    'summary': 'Theme Levelup',
    'category': 'Theme/Corporate',
    'version': '16.0.0.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'website_sale', 'website_sale_wishlist',
                'website_blog'],
    'data': [
        'views/blog.xml',
        'views/portfolio.xml',
        'views/about_us.xml',
        'views/footer.xml',
        'views/header.xml',
        'views/layout.xml',
        'views/contact_us.xml',
        'views/team.xml',
        'views/service.xml',
        'views/snippets/snippet.xml',
        'views/snippets/awards.xml',
        'views/snippets/service.xml',
        'views/snippets/feature.xml',
        'views/snippets/excited.xml',
        'views/snippets/testimonial.xml',
        'views/snippets/client.xml',
        'views/snippets/banner.xml',
        'views/snippets/about.xml',
        'views/snippets/gallery.xml',
        'views/snippets/blog.xml',
        'views/shop.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'https://fonts.googleapis.com/css2?family=Red+Hat+Display:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700&display=swap',
            'theme_levelup/static/src/js/owl.carousel.js',
            'theme_levelup/static/src/css/animate.min.css',
            'theme_levelup/static/src/css/owl.carousel.min.css',
            'theme_levelup/static/src/css/owl.theme.default.min.css',
            'theme_levelup/static/src/css/style.css',
            'theme_levelup/static/src/css/font.css',
            'theme_levelup/static/src/js/index.js',
            'theme_levelup/static/src/js/owl.carousel.min.js',
            'theme_levelup/static/src/js/script.js',
            'theme_levelup/static/src/xml/snippet.xml',
            'theme_levelup/static/src/js/blog.js',
            'theme_levelup/static/src/js/options.js',
            'theme_levelup/static/src/js/banner_counter.js',
            'theme_levelup/static/src/js/bootstrap-dropdownhover.js',
            'theme_levelup/static/src/js/bootstrap-dropdownhover.min.js',
            'theme_levelup/static/src/css/bootstrap.css',
            'theme_levelup/static/src/css/bootstrap-dropdownhover.css',
            'theme_levelup/static/src/css/bootstrap-dropdownhover.min.css',
            'http://code.jquery.com/jquery-1.11.1.min.js',
            'https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js',
        ],
    },
    'images': [

    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
