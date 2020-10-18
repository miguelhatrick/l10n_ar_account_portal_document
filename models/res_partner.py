# Copyright (C)
# Copyright 2020- Miguel Hatrick(<http://www.dacosys.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import pdb
from datetime import datetime

from odoo import fields, models, api


class ResCustomPartner(models.Model):
    """Copy VAT and set l8n_ar document_id"""
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        """Custom function to copy the vat into l8n_ar document_id"""

        # if vat is available, set the DNI data as a copy of it
        if vals['vat']:
            vals['main_id_number'] = vals['vat']
            vals['main_id_category_id'] = 35
            vals['afip_responsability_type_id'] = 6

        result = super(ResCustomPartner, self).create(vals)
        return result

    # select id, vat, main_id_number, main_id_category_id,afip_responsability_type_id from res_partner where name like '%hatrick%'

    # _event = self.env['event.event'].search([('id', '=', vals['event_id'])])[0]
    # _map = False
    #
    # # if event has a generator_id we are interested in this
    # if len(_event.event_generator_id):
    #     _member = self.env['res.partner'].search([('id', '=', vals['partner_id'])])[0]
    #     _location = _event.address_id
    #
    #     if not len(_member) or not len(_location):
    #         raise ValidationError('Partner or Location null in creation (EventRegistration)')
    #
    #     _map = self.env['climbing_gym.member_access_package'].get_first_available(_member, _location)
    #
    #     if not _map:
    #         raise ValidationError('The member package has no more credits / active packets (EventRegistration)')
    #
    #     if _map.calculate_remaining_credits():
    #         vals['member_access_package_id'] = _map.id
