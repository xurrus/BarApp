from odoo import models, fields

class ProductModel(models.Model):
    _name = 'bar_app.product_model'
    _description = 'This is the product model'
    
    name = fields.Char(string="Name",help="Name of the product",requiered=True,index=True)
    photo = fields.Binary()
    price = fields.Float(string="Price €")
    description = fields.Text(string="Description",help="Description of the product",requiered=True)
    category = fields.Many2one("bar_app.category_model",string="Categorie")
    ingredients = fields.Many2many("bar_app.ingredient_model",string="List of ingredients",relation="bar_app_products2ingredients")