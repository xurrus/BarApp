from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

class ProductModel(models.Model):
    _name = 'bar_app.invoice_model'
    _description = 'This is the invoice model'
    _order = 'ref'

    ref = fields.Integer(string="Invoice number",index=True)
    client = fields.Char(string="Client",help="Client name",requiered=True)
    lines = fields.Many2many("bar_app.line_model",relation="bar_app_invoice2lines",string="List of lines")
    base = fields.Float(string="Base price €",compute="_computeBase",help="Price of the invoice without VAT")
    vat = fields.Selection([ ('0','0'),('4','4'),('11','11'),('21','21'),],string='VAT',help="VAT number % to add to base price")
    total = fields.Float(string="Total price €",help="Final price including VAT",compute="_computeTotal")
    creationDate = fields.Datetime(string="Creation date",default=lambda self: datetime.today())

    @api.depends('lines','lines.product_id','lines.quantity')
    def _computeBase(self):
        for rec in self:
            rec.base = 0
            for l in rec.lines:
                rec.base += l.product_id.price*l.quantity

    @api.depends('base','vat')
    def _computeTotal(self):
        self.total = self.base+(int(self.vat)*self.base/100)

    #####api
    # def _computeRefIncrement(self):
    #     for rec in self:
    #         pass