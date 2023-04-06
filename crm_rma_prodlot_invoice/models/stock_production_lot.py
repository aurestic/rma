# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2015 Vauxoo
#    Author: Yanina Aular, Osval Reyes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import _, api, fields, models


class StockProductionLot(models.Model):

    _inherit = 'stock.production.lot'

    invoice_line_id = fields.Many2one('account.invoice.line',
                                      string='Customer Invoice Line',
                                      help="Invoice Line Of "
                                      "Product to Customer Invoice")

    lot_complete_name = fields.Char(compute="_get_lot_complete_name",
                                    string="Complete Lot Name")

    @api.multi
    @api.depends('invoice_line_id', 'name')
    def _get_lot_complete_name(self):
        for lot in self:
            lot.lot_complete_name = _("%s - Lot Number: %s - %s") % (
                lot.invoice_line_id.invoice_id.number,
                lot.name or _('No lot number'),
                lot.invoice_line_id.name,
            )
