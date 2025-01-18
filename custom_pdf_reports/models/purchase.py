from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    dispatch_through = fields.Char(string="Dispatch Through")