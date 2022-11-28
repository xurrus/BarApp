from odoo import models, fields,api
from odoo.exceptions import ValidationError

class IngredientModel(models.Model):
    _name = 'bar_app.ingredient_model'
    _description = 'This is the ingredient model'
    _sql_constraints = [('bar_app_ingredientname',
                        'UNIQUE (name)',
                        'There cannot be two ingredients with the same name!!'),
                        ]
    
    name = fields.Char(string="Name",help="Name of the ingredient",requiered=True,index=True)
    typeI = fields.Selection([ ('Fats and oils','Fats and oils'),('Eggs or Milk','Eggs or Milk'),('Fruits','Fruits'),('Vegetables','Vegetables'),('Grain, nuts','Grain, nuts'),('Herbs and spices','Herbs and spices'),('Meat','Meat'),('Fish','Fish'),('Pasta','Pasta'),('Others','Others'),],string='Type of ingredient')
    observations = fields.Text(string="Observations", help="Additional description for the ingredient")
    products = fields.Many2many("bar_app.product_model",string="Products with this ingredient",relation="bar_app_products2ingredients")

    @api.constrains("name")
    def _nameLength(self):
        if len(self.name) < 3:
            raise ValidationError("The length of the ingredient name must have 3 characters")