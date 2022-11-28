from odoo import models, fields,api
from odoo.exceptions import ValidationError

class ProductModel(models.Model):
    _name = 'bar_app.product_model'
    _description = 'This is the product model'
    _sql_constraints = [('bar_app_productname',
                        'UNIQUE (name)',
                        'There cannot be two products with the same name!!'),
                        ]
    
    name = fields.Char(string="Name",help="Name of the product",requiered=True,index=True)
    photo = fields.Binary()
    price = fields.Float(string="Price €")
    description = fields.Text(string="Description",help="Description of the product",requiered=True)
    category = fields.Many2one("bar_app.category_model",string="Categorie")
    ingredients = fields.Many2many("bar_app.ingredient_model",string="List of ingredients",relation="bar_app_products2ingredients")

    @api.constrains("name")
    def _nameLength(self):
        if len(self.name) < 5:
            raise ValidationError("The length of the product name must have 5 characters")
    
    @api.constrains("price")
    def _priceValue(self):
        if self.price < 1.50:
            raise ValidationError("The price of the product must be at least 1.50")