from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineModel(models.Model):
     _name = 'bar_app.line_model'
     _description = 'Line Model'
     _rec_name = 'fullName'

     order_id = fields.Many2one("bar_app.order_model",string="Order",help="Order reference",required=True)
     product_id =fields.Many2one("bar_app.product_model",string="Product", help="Product name",required=True)
     quantity = fields.Integer(string="Quantity",required=True,default=1,help="Quantity for this line")
     fullName = fields.Char(string='Full Name', compute='_compute_fields_combination')
     observations = fields.Text(string="Observations",help="Observations of this line")

     @api.depends('order_id', 'product_id')
     def _compute_fields_combination(self):
          for rec in self:
               if rec.order_id:
                    rec.fullName = str(rec.order_id.table) + ' : '+ str(rec.quantity) + " de " + str(rec.product_id.name)
               else:
                    rec.fullName = 'No order:' + str(rec.quantity) + " de " + str(rec.product_id.name)