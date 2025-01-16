from odoo import models, fields, api


class PartnerCustom(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Char('Arabic Name')
    arabic_street = fields.Char()
    arabic_street2 = fields.Char()
    arabic_zip = fields.Char()
    arabic_city = fields.Char()
    arabic_country = fields.Char()
    arabic_state = fields.Char()
    cr_number = fields.Char('CR No')
    p_vendor_id = fields.Char('Aramco Vendor ID')



