from odoo import models, fields, api, _


class CompanyCustom(models.Model):
    _inherit = 'res.company'

    arabic_name = fields.Char(store=True, readonly=False)
    arabic_street = fields.Char(string='Arabic Street...')
    arabic_street2 = fields.Char(string='Arabic Street2...')
    arabic_city = fields.Char(string='Arabic City')
    arabic_zip = fields.Char(string='Arabic Zip')
    arabic_phone = fields.Char(string='Arabic Phone')
    c_vendor_id = fields.Char('Aramco Vendor ID')
