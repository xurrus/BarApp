from odoo import models, fields,api
from datetime import datetime

class OrderModel(models.Model):
    _name = 'bar_app.order_model'
    _description = 'This is the order model'
    _sql_constraints = [('bar_app_table',
                        'UNIQUE (table)',
                        'There cannot be two tables actives with the same name'),
                        ]
    _rec_name = 'table'

    table = fields.Char(string="Table",help="Table of the order",required=True,index=True)
    state = fields.Selection([('A','Active'),('C','Confirmed'),],string="State",help="Is the order active yet?",default='A')
    client = fields.Char(string="Client",help="Client of the order",required=True)
    waiter = fields.Char(string="Waiter",help="Waiter of the order",compute="_computeUser")
    price = fields.Float(string="Price €",compute="_calculatePrice")
    date = fields.Date(string="Date",required=True,default=datetime.now(),help="Date")
    lines = fields.One2many("bar_app.line_model","order_id",string="Lines of products")
    numLines = fields.Integer(string="Number of lines",help="Number of lines in this order",compute="_totalLines",store=True)

    @api.depends("lines.product_id","lines.quantity")
    def _calculatePrice(self):
        for rec in self:
            rec.price = 0
            for linea in rec.lines:
                rec.price += linea.product_id.price*linea.quantity

    @api.depends("lines")
    def _totalLines(self):
        self.numLines = len(self.lines)

    def changeState(self):
        if self.state == 'C':
            self.state = 'A'
        else:
            #CAMBIAMOS EL ESTADO
            self.state = 'C'
            #CREAMOS INVOICE SOLO CON CLIENTE
            invoice = {}
            invoice["client"] = self.client
            newInvoice = self.env["bar_app.invoice_model"].sudo().create(invoice)
            #CREAMOS LINES INVOICE
            for linea in self.lines:
                lineinvoice = {}
                lineinvoice["refId"] = newInvoice.id
                lineinvoice["quantity"] = linea.quantity
                lineinvoice["product"] = linea.product_id.id
                self.env["bar_app.line_invoice_model"].sudo().create(lineinvoice)

            return self.state

    @api.depends('client')
    def _computeUser(self):
        for rec in self:
            rec.waiter = self.env.user.name