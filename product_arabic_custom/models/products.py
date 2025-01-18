# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    arabic_name = fields.Text()
    name = fields.Char('Product Name', required=True,  tracking=True)

class CompanyHeaderfootr(models.Model):
    _inherit = 'res.company'

    header_img = fields.Binary('Header Image ')
    footer_img = fields.Binary('Footer Image ')
    company_seal_img = fields.Binary("Company Seal Image")
    approve_sign_img = fields.Binary("Approve Sign Image")
