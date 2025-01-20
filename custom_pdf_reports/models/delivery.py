from odoo import models,fields

class StockPicking(models.Model):
    _inherit = "stock.picking"

    driver_partner_id = fields.Many2one('res.partner', string="Driver")
    vehicle_no = fields.Char(string="Vehicle No.")