# Copyright (C)
# Copyright 2020- Miguel Hatrick(<http://www.dacosys.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import logging
import pdb

from odoo import fields, models, api


_logger = logging.getLogger(__name__)


class ResCustomPartner(models.Model):
    """Copy VAT and set l8n_ar document_id"""
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        """Custom function to copy the vat into l8n_ar document_id"""

        result = super(ResCustomPartner, self).create(vals)
        return result

    @api.multi
    def write(self, values):
        _logger.info('if vat is available, set the DNI data as a copy of it ... ')
        # if vat is available, set the DNI data as a copy of it
        if 'vat' in values and values['vat'] and not self.main_id_number:
            _logger.info('Copying VAT ID to Document_ID ... ')

            values['main_id_number'] = values['vat']
            values['main_id_category_id'] = 35
            values['afip_responsability_type_id'] = 6

        result = super(ResCustomPartner, self).write(values)
        # Update

        return result



    # select id, vat, main_id_number, main_id_category_id,afip_responsability_type_id from res_partner where name like '%hatrick%'

    # _event = self.env['event.event'].search([('id', '=', values['event_id'])])[0]
    # _map = False
    #
    # # if event has a generator_id we are interested in this
    # if len(_event.event_generator_id):
    #     _member = self.env['res.partner'].search([('id', '=', values['partner_id'])])[0]
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
    #         values['member_access_package_id'] = _map.id
