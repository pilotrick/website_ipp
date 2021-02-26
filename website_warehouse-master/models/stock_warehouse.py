# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class WareHouse(models.Model):
    _inherit = 'stock.warehouse'

    show_website = fields.Boolean("Display on Website")
