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
     orderClient = fields.Char(string="Order client",help="Client of the order",compute="_computeOrderClient")

     @api.depends('order_id', 'product_id')
     def _compute_fields_combination(self):
          for rec in self:
               if rec.order_id:
                    rec.fullName = str(rec.order_id.table) + ' : '+ str(rec.quantity) + " de " + str(rec.product_id.name)
               else:
                    rec.fullName = 'No order:' + str(rec.quantity) + " de " + str(rec.product_id.name)

     #boton de barman para confirmar bebida
     def drinkToDone(self):
          #SI ESTA O, PASA A D
          if self.state == 'O':
            self.state = 'D'
          return {
               'name': ('Barman Lines'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'bar_app.line_model',
               'domain':[('product_id.category.location','=','B'),('state','=','O'),('order_id.state','=','A')],
               'view_id':False,
               'views':[(self.env.ref('bar_app.line_tree_barman').id,'tree'),(self.env.ref('bar_app.line_form_barman').id, 'form')],
               'type':'ir.actions.act_window'
          }

     #boton de cooker para confirmar plato
     def productToDone(self):
          #SI ESTA O, PASA A D
          if self.state == 'O':
            self.state = 'D'
          return {
               'name': ('Cooker Lines'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'bar_app.line_model',
               'domain':[('product_id.category.location','=','K'),('state','=','O'),('order_id.state','=','A')],
               'view_id':False,
               'views':[(self.env.ref('bar_app.line_tree_cooker').id,'tree'),(self.env.ref('bar_app.line_form_cooker').id, 'form')],
               'type':'ir.actions.act_window'
          }

     #boton de camarero para entregar linea
     def productToFinished(self):
          #SI ESTA D, PASA A F
          if self.state == 'D':
            self.state = 'F'
          return {
               'name': ('Waiter Lines'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'bar_app.line_model',
               'domain':[('state','=','D'),('order_id.state','=','A')],
               'view_id':False,
               'views':[(self.env.ref('bar_app.line_tree_waiter').id,'tree'),(self.env.ref('bar_app.line_form_waiter').id, 'form')],
               'type':'ir.actions.act_window'
          }

     @api.depends('order_id')
     def _computeOrderClient(self):
          for rec in self:
               rec.orderClient = rec.order_id.client