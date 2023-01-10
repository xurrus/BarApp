from odoo import models, fields,api
from odoo.exceptions import ValidationError

class CategoryModel(models.Model):
    _name = 'bar_app.category_model'
    _description = 'This is the category model'
    _sql_constraints = [('bar_app_categoryname',
                        'UNIQUE (name)',
                        'There cannot be two categories with the same name!!'),
                        ]
    _rec_name = 'full_name'
    _order = 'full_name'

    name = fields.Char(string="Name",help="Name of the category",requiered=True,index=True)
    full_name = fields.Char(string="Full name",compute="_computeFullName")
    products = fields.One2many("bar_app.product_model","category",string="List of products")
    photo = fields.Binary(string="Image")
    parent_id = fields.Many2one("bar_app.category_model",string="Category parent",index=True)
    numProducts = fields.Integer(string="Number of products",help="Number of products in this category",compute="_totalProducts",store=True)
        

    @api.constrains("name")
    def _nameLength(self):
        if len(self.name) < 5:
            raise ValidationError("The length of the category name must have 5 characters")

    @api.depends("products")
    def _totalProducts(self):
        self.numProducts = len(self.products)

    @api.depends('name','parent_id.full_name')
    def _computeFullName(self):
        for category in self:
            if category.parent_id:
                category.full_name = " %s / %s" % (category.parent_id.full_name,category.name)
            else:
                category.full_name = category.name