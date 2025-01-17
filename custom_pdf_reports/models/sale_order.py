from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    subject_ref = fields.Char(string="Subject")
    attn_partner_id = fields.Many2one('res.partner', string="ATTN Contact")