# -*- coding: utf-8 -*-
{
    'name': "bar_app",

    'summary': """
        Aplication to control de different bars""",

    'description': """
        This aplication to control a bar
    """,

    'author': "David Gozalvez",
    'website': "http://www.iscaa.es",

    # Categorbar can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/bar_app_security.xml',
        'security/ir.model.access.csv',
        'views/ingredient_view.xml',
        'views/category_view.xml',
        'views/product_view.xml',
        'views/order_view.xml',
        'views/line_view.xml',
        'views/line_view_waiter.xml',
        'views/line_view_cooker.xml',
        'views/line_view_barman.xml',
        'views/invoice_view.xml',
        'views/line_invoice_view.xml',
        'report/invoice_pdf.xml',
        'report/report3.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
