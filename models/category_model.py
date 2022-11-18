from odoo import models, fields

class CategoryModel(models.Model):
    _name = 'bar_app.category_model'
    _description = 'This is the category model'

    name = fields.Char(string="Name",help="Name of the category",requiered=True,index=True)
    products = fields.One2many("bar_app.product_model","category",string="List of products")
        

    