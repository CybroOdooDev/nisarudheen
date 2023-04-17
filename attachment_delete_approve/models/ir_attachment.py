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

from odoo import models, api
from odoo.exceptions import UserError


class IrAttachment(models.Model):
    """This model inherited for generating
    attachment delete approval requests."""
    _inherit = 'ir.attachment'


    @api.model
    def models(self, value):
        """This function Was used to checking active user allowed to
        access this models document. """
        flag = False
        attachment_id = self.env['ir.attachment'].browse(value)
        model = self.env['ir.config_parameter'].sudo().get_param(
            'attachment_delete_approve.model_ids')
        models = self.env['ir.model'].sudo().browse(eval(model))
        for rec in models:
            if attachment_id.res_model == rec.model:
                flag = True
        return flag

    @api.model
    def get_user(self,record):
        """This function was created for checking our login user
        (admin or user) and delete request already send or not."""
        is_admin = self.env.user.has_group(
            'attachment_delete_approve.approve_access')
        attachment = self.env['ir.attachment'].browse(record)
        value = True if self.env["attachment.approval"].search([(
            'document_id', '=', attachment.id)]) else False
        return is_admin, value

    def all_models(self):
        """This function was used to checking user access all models or not"""
        all_model = self.env['ir.config_parameter'].sudo().get_param(
            'res.config.settings.all_models')
        if all_model:
            return True
        else:
            return False

    def unlink(self):
        """This function is used if the user has no rights to delete 
          attachments. but he wanted to delete that attachment, 
          so do that by creating an approval request to the 
          admin from the user"""
        is_admin = self.env.user.has_group(
            'attachment_delete_approve.approve_access')
        if is_admin:
            super().unlink()
        else:
            all_model = self.env['ir.config_parameter'].sudo().get_param(
                 'res.config.settings.all_models')
            if all_model:
                self.env['attachment.approval'].sudo().create({
                    'name': "Attachment delete approve",
                    'request_owner': self.env.user.id,
                    'reference': self.res_name,
                    'document_id': self.id,
                    'res_model': self.res_model,
                    'res_id': self.res_id
                        })
            else:
                model = self.env['ir.config_parameter'].sudo().get_param(
                    'attachment_delete_approve.model_ids')
                for rec in self.env['ir.model'].sudo().browse(eval(model)):
                    if self.res_model == rec.model:
                        self.env['attachment.approval'].sudo().create({
                            'name': "Attachment delete approve",
                            'request_owner': self.env.user.id,
                            'reference': self.res_name,
                            'document_id': self.id,
                            'res_model': self.res_model,
                            'res_id': self.res_id,
                        })
            return True
