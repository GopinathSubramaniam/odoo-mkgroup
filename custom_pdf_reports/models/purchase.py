from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    dispatch_through = fields.Char(string="Dispatch Through")
    contact_partner_id = fields.Many2one('res.partner', string="Contact Person", default=lambda self: self.env.user.partner_id.id)

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    remarks = fields.Char(string="Remarks")