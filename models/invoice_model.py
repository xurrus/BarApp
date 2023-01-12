from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

class ProductModel(models.Model):
    _name = 'bar_app.invoice_model'
    _description = 'This is the invoice model'
    _order = 'ref'

    ref = fields.Integer(string="Invoice number",index=True,default = lambda self : self._computeRefIncrement())
    client = fields.Char(string="Client",help="Client name",requiered=True)
    order = fields.Many2one("bar_app.order_model",string="Order")
    base = fields.Float(string="Base price €",compute="_computeBase",help="Price of the invoice without VAT")
    vat = fields.Selection([ ('0','0'),('4','4'),('11','11'),('21','21'),],string='VAT',help="VAT number % to add to base price")
    total = fields.Float(string="Total price €",help="Final price including VAT",compute="_computeTotal")
    creationDate = fields.Datetime(string="Creation date",default=lambda self: datetime.today())
    state = fields.Selection([('A','Active'),('C','Confirmed'),],string="State",help="Is the invoice active yet?",defalut='A')

    @api.depends('order','order.lines.product_id','order.lines.quantity')
    def _computeBase(self):
        for rec in self:
            rec.base = rec.order.price

    @api.depends('base','vat')
    def _computeTotal(self):
        for rec in self:
            rec.total = rec.base+(int(rec.vat)*rec.base/100)

    def _computeRefIncrement(self):
            allInvoices = self.env["bar_app.invoice_model"].sudo().search_read([],["ref"])
            if len(allInvoices) > 0:
                lastInvoice = allInvoices[-1]
                return int(lastInvoice['ref']) + 1 
            else:
                return 1

    def confirmInvoice(self):
        self.state = 'C'