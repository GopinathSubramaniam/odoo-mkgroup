{
    "name": "Custom PDF Reports",
    "version": "1.0",
    "author": "Sygmetiv",
    "website": "https://www.sygmetiv.com",
    "depends": ['base', 'web', 'account', 'l10n_sa', 'l10n_sa_edi' ,'sale_management'],
    "data": [
        "views/layouts.xml",
        "views/sale_form.xml",
        "views/invoice_report.xml",
        "views/quotation_report.xml",
        "views/purchase_report.xml",
    ],
    'installable': True,
    'application': False,
}
