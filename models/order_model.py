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

    table = fields.Char(string="Table",help="Table of the order",requiered=True,index=True)
    active = fields.Boolean(string="Is active",help="Is the order active?")
    client = fields.Char(string="Client",help="Client of the order",requiered=True)
    waiter = fields.Char(string="Waiter",help="Waiter of the order")
    price = fields.Float(string="Price €",compute="_calculatePrice")
    date = fields.Date(string="Date",required=True,default=datetime.now(),help="Date")
    lines = fields.One2many("bar_app.line_model","order_id",string="Lines of products")

    @api.depends("lines.product_id","lines.quantity")
    def _calculatePrice(self):
        self.price = 0
        for linea in self.lines:
            self.price += linea.product_id.price*linea.quantity


    