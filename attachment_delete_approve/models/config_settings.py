# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import models, fields, api


class ConfigurationSettings(models.TransientModel):
    """This model inherited for creating
    a new field models and all model"""
    _inherit = "res.config.settings"
    _description = "Settings Inherit"

    attachment_delete_model = fields.Boolean(
        string='Attachment Delete Models',
        config_parameter="res.config.settings.attachment_delete")
    all_models = fields.Boolean(string="Select All Models",
                                config_parameter=
                                "res.config.settings.all_models")
    model_ids = fields.Many2many('ir.model',
                                 domain="[('is_mail_thread', '=', True)]",
                                 string='Models'
                                )

    def set_values(self):
        """This function used to store field values to config parameter"""
        res = super(ConfigurationSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'attachment_delete_approve.model_ids', self.model_ids.ids)
        return res

    @api.model
    def get_values(self):
        """This function helps to getting a values from config parameter"""
        res = super(ConfigurationSettings, self).get_values()
        models = self.env['ir.config_parameter'].sudo().get_param(
            'attachment_delete_approve.model_ids')
        if models :
            list_model = eval(models)
        else:
            list_model = False
        model_id = self.env['ir.model'].browse(list_model)
        res.update(model_ids=[(fields.Command.set(model_id.ids))
                              ])
        return res