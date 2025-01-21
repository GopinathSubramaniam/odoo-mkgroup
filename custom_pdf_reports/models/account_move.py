from odoo import fields,models,api


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_name_invoice_report(self):
        res = super()._get_name_invoice_report()
        return 'custom_pdf_reports.report_invoice_document_inherit'
    
    def get_delivery_note_names(self):
        stock_pickings = []
        for line in self.invoice_line_ids:
            if line.sale_line_ids:
                stock_pickings = line.sale_line_ids.order_id.picking_ids.filtered(lambda picking: picking.state in ('assigned,done'))
                break
        delivery_notes = ', '.join([picking.name for picking in stock_pickings])
        return delivery_notes or ''

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # To show tax amount as a monetary field
    line_tax_amount = fields.Monetary(
        string="Tax Amount",
        compute="_compute_line_tax_amount",
        currency_field="currency_id",
        store=True,
        help="The total tax amount for this line."
    )

    @api.depends('l10n_gcc_invoice_tax_amount')
    def _compute_line_tax_amount(self):
        for record in self:
            record.line_tax_amount = record.l10n_gcc_invoice_tax_amount

    @api.depends('price_subtotal', 'price_total')
    def _compute_tax_amount(self):
        super()._compute_tax_amount()
        AccountTax = self.env['account.tax']
        for line in self:
            line.l10n_gcc_invoice_tax_amount = line.l10n_gcc_invoice_tax_amount or 0
            if (
                line.move_id.country_code == 'SA'
                and line.move_id.is_invoice(include_receipts=True)
                and line.display_type == 'product'
            ):
                base_line = line.move_id._prepare_product_base_line_for_taxes_computation(line)
                AccountTax._add_tax_details_in_base_line(base_line, line.company_id)
                AccountTax._round_base_lines_tax_details([base_line], line.company_id)
                line.l10n_gcc_invoice_tax_amount = sum(
                    tax_data['tax_amount_currency']
                    for tax_data in base_line['tax_details']['taxes_data']
                    if not tax_data['tax'].l10n_sa_is_retention
                )