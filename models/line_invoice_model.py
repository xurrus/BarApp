from odoo import models, fields, api

class LineInvoiceModel(models.Model):
    _name = 'bar_app.line_invoice_model'
    _description = 'This is a line invoice model.'

    refId = fields.Many2one("bar_app.invoice_model", string="Invoice reference")
    quantity = fields.Integer(string="Quantity",help="Quantity of the product.",default=1)
    product = fields.Many2one("bar_app.product_model", string="Product")
    description = fields.Html(string="Description",help="Description of the product")