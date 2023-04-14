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


from odoo import fields, models


class AttachmentApproval(models.Model):
    """This model created for storing a approval request of approver or admin"""
    _name = 'attachment.approval'

    name = fields.Char(string='Approval Subject')
    request_owner = fields.Many2one('res.users', string='Request Owner')
    dates = fields.Date(string='Date', default=fields.Date.today())
    reference = fields.Text(string='Reference')
    document_id = fields.Many2one('ir.attachment')
    res_model = fields.Text(string='Model')
    res_id = fields.Integer(string='Record')

    def unlink_record(self):
        """This function used to deleting
        a corresponding record in attachments"""
        record = self.env['ir.attachment'].search([(
            "res_model", '=', self.res_model),
            ("res_id", '=', self.res_id), ('name', '=', self.document_id.name)])
        record.unlink()