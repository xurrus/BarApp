from odoo import models, fields

class OrderModel(models.Model):
    _name = 'bar_app.order_model'
    _description = 'This is the order model'
    
    table = fields.Char(string="Table",help="Table of the order",requiered=True,index=True)
    active = fields.Boolean(string="Is active",help="Is the order active?")
    client = fields.Char(string="Client",help="Client of the order",requiered=True)
    pax = fields.Float(string="Price €",requiered=True)
    waiter = fields.Char(string="Waiter",help="Waiter of the order")
    #products = fields.One2many("bar_app.product_model","order",string="List of products")

    