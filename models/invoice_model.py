from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

class ProductModel(models.Model):
    _name = 'bar_app.invoice_model'
    _description = 'This is the invoice model'
    _order = 'ref'
    _rec_name = 'ref'

    ref = fields.Integer(string="Invoice number",index=True,default = lambda self : self._computeRefIncrement())
    client = fields.Char(string="Client",help="Client name",required=True)
    lines = fields.One2many("bar_app.line_invoice_model", "refId" , string="Lines")
    base = fields.Float(string="Base price €",compute="_computeBase",help="Price of the invoice without VAT")
    vat = fields.Selection([ ('0','0'),('4','4'),('10','10'),('21','21'),],string='VAT',help="VAT number % to add to base price",default='21')
    total = fields.Float(string="Total price €",help="Final price including VAT",compute="_computeTotal")
    creationDate = fields.Datetime(string="Creation date",default=lambda self: datetime.today())
    state = fields.Selection([('A','Active'),('C','Confirmed'),],string="State",help="Is the invoice active yet?",defalut='A')

    @api.depends('lines','lines.product','lines.quantity')
    def _computeBase(self):
        for rec in self:
            rec.base = 0
            for l in rec.lines:
                rec.base += l.product.price*l.quantity

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