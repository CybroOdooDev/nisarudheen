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


class IrAttachment(models.Model):
    """This model inherited for generating
    attachment delete approval requests."""
    _inherit = 'ir.attachment'

    @api.model
    def models(self,id):
        print(id)
        attachment_id = self.env['ir.attachment'].browse(id)
        print(attachment_id.res_model)
        model = self.env['ir.config_parameter'].sudo().get_param(
            'attachment_delete_approve.model_ids')
        models = self.env['ir.model'].sudo().browse(eval(model))

        print(self.env.context)

    def get_user(self):
        """This function was created for checking our login user
        (admin or user)."""
        is_admin = self.env.user.has_group(
            'attachment_delete_approve.approve_access')
        return is_admin

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
