from odoo import models, fields,api
from odoo.exceptions import ValidationError

class CategoryModel(models.Model):
    _name = 'bar_app.category_model'
    _description = 'This is the category model'
    _sql_constraints = [('bar_app_categoryname',
                        'UNIQUE (name)',
                        'There cannot be two categories with the same name!!'),
                        ]

    name = fields.Char(string="Name",help="Name of the category",requiered=True,index=True)
    products = fields.One2many("bar_app.product_model","category",string="List of products")
        

    @api.constrains("name")
    def _nameLength(self):
        if len(self.name) < 5:
            raise ValidationError("The length of the category name must have 5 characters")