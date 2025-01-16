from odoo import fields,models,api

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    tax_amount = fields.Monetary(
        string="Tax Amount",
        compute="_compute_tax_amount",
        currency_field="currency_id",
        store=True,
        help="The total tax amount for this line."
    )

    @api.depends('tax_ids', 'price_unit', 'quantity', 'move_id.partner_id', 'move_id.currency_id', 'move_id.move_type')
    def _compute_tax_amount(self):
        for line in self:
            total_tax_amount = 0.0
            if line.move_id.move_type in ['out_invoice', 'in_invoice']:  # Only for invoices
                for tax in line.tax_ids:
                    # Compute tax using Odoo's tax engine
                    tax_result = tax.compute_all(
                        price_unit=line.price_unit,
                        currency=line.currency_id,
                        quantity=line.quantity,
                        product=line.product_id,
                        partner=line.move_id.partner_id
                    )
                    total_tax_amount += sum(t['amount'] for t in tax_result['taxes'])
            line.tax_amount = total_tax_amount