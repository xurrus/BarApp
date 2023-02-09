from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineModel(models.Model):
     _name = 'bar_app.line_model'
     _description = 'Line Model'
     _rec_name = 'fullName'

     order_id = fields.Many2one("bar_app.order_model",string="Order",help="Order reference",required=True,ondelete='cascade')
     product_id =fields.Many2one("bar_app.product_model",string="Product", help="Product name",required=True)
     quantity = fields.Integer(string="Quantity",required=True,default=1,help="Quantity for this line")
     fullName = fields.Char(string='Full Name', compute='_compute_fields_combination')
     observations = fields.Text(string="Observations",help="Observations of this line")
     state = fields.Selection([('O','Ordered'),('D','Done'),('F','Finished')],string="State of the line",help="Is the order active yet?",default='O')

     @api.depends('order_id', 'product_id')
     def _compute_fields_combination(self):
          for rec in self:
               if rec.order_id:
                    rec.fullName = str(rec.order_id.table) + ' : '+ str(rec.quantity) + " de " + str(rec.product_id.name)
               else:
                    rec.fullName = 'No order:' + str(rec.quantity) + " de " + str(rec.product_id.name)

     def stateToDone(self):
          #SI ESTA O, PASA A D
          if self.state == 'O':
            self.state = 'D'

     def stateToFinished(self):
          #SI ESTA D, PASA A F
          if self.state == 'D':
            self.state = 'F'