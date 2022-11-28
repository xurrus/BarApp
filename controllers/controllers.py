# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json


class barApp(http.Controller):

    @http.route('/bar_app/categories',auth="public",type="http")
    def categories(self,**kw):
        taskdata = http.request.env["bar_app.category_model"].sudo().search_read([],["name","products"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar_app/products',auth="public",type="http")
    def products(self,**kw):
        taskdata = http.request.env["bar_app.product_model"].sudo().search_read([],["name","description","price","category","ingredients"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar_app/ingredients',auth="public",type="http")
    def ingredients(self,**kw):
        taskdata = http.request.env["bar_app.ingredient_model"].sudo().search_read([],["name","typeI","observations","products"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")


    # @http.route('/bar_app/bar_app', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"
    # @http.route('/bar_app/bar_app/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('bar_app.listing', {
    #         'root': '/bar_app/bar_app',
    #         'objects': http.request.env['bar_app.bar_app'].search([]),
    #     })
    # @http.route('/bar_app/bar_app/objects/<model("bar_app.bar_app"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('bar_app.object', {
    #         'object': obj
    #     })
