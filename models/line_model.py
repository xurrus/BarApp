from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineModel(models.Model):
     _name = 'bar_app.line_model'
     _description = 'Line Model'
     _rec_name = 'fullName'

     order_id = fields.Many2one("bar_app.order_model",string="Order",help="Order reference")
     product_id =fields.Many2one("bar_app.product_model",string="Product", help="Product name")
     quantity = fields.Integer(string="Quantity",required=True,default=1,help="Quantity for this line",default=1)
     fullName = fields.Char(string='Full Name', compute='_compute_fields_combination')

     @api.depends('order_id', 'product_id')
     def _compute_fields_combination(self):
          for rec in self:
               rec.fullName = str(rec.order_id.table) + ' : '+ str(rec.quantity) + " de " + str(rec.product_id.name)