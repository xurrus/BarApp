# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json,request


class barApp(http.Controller):

    #############################################################
    ####################### CATEGORY MODEL ########################
    #############################################################
    #GET one category by id
    @http.route('/bar_app/getCategory/<int:catid>',auth="public",type="http")
    def getCategory(self,catid=None,**kw):
        if catid:
            domain = [("id","=",catid)]
        else:
            domain = []
        taskdata = http.request.env["bar_app.category_model"].sudo().search_read(domain,["name","full_name","products","parent_id"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #GET all categories
    @http.route('/bar_app/getCategories',auth="public",type="http")
    def getCategories(self,**kw):
        taskdata = http.request.env["bar_app.category_model"].sudo().search_read([],["name","full_name","products","parent_id"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #POST one category
    @http.route('/bar_app/addCategory',auth="public",type="json",method="POST")
    def addCategory(self,**kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.category_model"].sudo().create(response)
            data = {  "status":201, "id":result.id, "full_name":result.full_name  }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #UPDATE one category
    @http.route('/bar_app/updateCategory',auth="public",type="json",method="PUT")
    def updateCategory(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.category_model"].sudo().search(domain)
            updated = cat.sudo().write(response)
            if (updated):
                data = {  "status":200, "result":cat.id, "full_name":cat.full_name }
            else:
                data = { "status":400, "result":"Category not modified"}
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #DELETE A CATEGORY
    @http.route('/bar_app/deleteCategory',auth="public",type="json",method="DELETE")
    def deleteCategory(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.category_model"].sudo().search(domain).unlink()
            data = {  "status":200, "result":"Category deleted" }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #############################################################
    ####################### INGREDIENT MODEL ########################
    #############################################################
    #GET one ingredient by id
    @http.route('/bar_app/getIngredient/<int:Ingredientid>',auth="public",type="http")
    def getIngredient(self,Ingredientid=None,**kw):
        if Ingredientid:
            domain = [("id","=",Ingredientid)]
        else:
            domain = []
        taskdata = http.request.env["bar_app.ingredient_model"].sudo().search_read(domain,["name","typeI","observations","products"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #GET all ingredients
    @http.route('/bar_app/getIngredients',auth="public",type="http")
    def getIngredients(self,**kw):
        taskdata = http.request.env["bar_app.ingredient_model"].sudo().search_read([],["name","typeI","observations","products"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #POST one ingredient
    @http.route('/bar_app/addIngredient',auth="public",type="json",method="POST")
    def addIngredient(self,**kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.ingredient_model"].sudo().create(response)
            data = {  "status":201, "id":result.id  }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #UPDATE one ingredient
    @http.route('/bar_app/updateIngredient',auth="public",type="json",method="PUT")
    def updateIngredient(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            ing = http.request.env["bar_app.ingredient_model"].sudo().search(domain)
            updated = ing.sudo().write(response)
            if (updated):
                data = {  "status":200, "result":ing.id }
            else:
                data = { "status":400, "result":"Ingredient not modified"}
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #DELETE A ingredient
    @http.route('/bar_app/deleteIngredient',auth="public",type="json",method="DELETE")
    def deleteIngredient(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.ingredient_model"].sudo().search(domain).unlink()
            data = {  "status":200, "result":"Ingredient deleted" }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #############################################################
    ####################### LINE MODEL ########################
    #############################################################
    #GET one line by id
    @http.route('/bar_app/getLine/<int:Lineid>',auth="public",type="http")
    def getLine(self,Lineid=None,**kw):
        if Lineid:
            domain = [("id","=",Lineid)]
        else:
            domain = []
        taskdata = http.request.env["bar_app.line_model"].sudo().search_read(domain,["order_id","product_id","quantity","fullName"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #GET all lines
    @http.route('/bar_app/getLines',auth="public",type="http")
    def getLines(self,**kw):
        taskdata = http.request.env["bar_app.line_model"].sudo().search_read([],["order_id","product_id","quantity","fullName"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #POST one line
    @http.route('/bar_app/addLine',auth="public",type="json",method="POST")
    def addLine(self,**kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.line_model"].sudo().create(response)
            data = {  "status":201, "id":result.id, "full_name":result.fullName}
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #UPDATE one line
    @http.route('/bar_app/updateLine',auth="public",type="json",method="PUT")
    def updateLine(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            line = http.request.env["bar_app.line_model"].sudo().search(domain)
            updated = line.sudo().write(response)
            if (updated):
                data = {  "status":200, "result":line.id ,"full_name":line.fullName}
            else:
                data = { "status":400, "result":"Line not modified"}
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #DELETE A line
    @http.route('/bar_app/deleteLine',auth="public",type="json",method="DELETE")
    def deleteLine(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.line_model"].sudo().search(domain).unlink()
            data = {  "status":200, "result":"Line deleted" }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data


    #############################################################
    ####################### ORDER MODEL ########################
    #############################################################
    #GET one order by id
    @http.route('/bar_app/getOrder/<int:Orderid>',auth="public",type="http")
    def getOrder(self,Orderid=None,**kw):
        if Orderid:
            domain = [("id","=",Orderid)]
        else:
            domain = []
        taskdata = http.request.env["bar_app.order_model"].sudo().search_read(domain,["table","client","state","waiter","price","lines","date"])
        for t in taskdata:
            t['date'] = t['date'].isoformat()
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #GET all orders
    @http.route('/bar_app/getOrders',auth="public",type="http")
    def getOrders(self,**kw):
        taskdata = http.request.env["bar_app.order_model"].sudo().search_read([],["table","client","state","waiter","price","lines","date"])
        for t in taskdata:
            t['date'] = t['date'].isoformat()
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #POST one order
    @http.route('/bar_app/addOrder',auth="public",type="json",method="POST")
    def addOrder(self,**kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.order_model"].sudo().create(response)
            data = {  "status":201, "id":result.id  }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #UPDATE one order
    @http.route('/bar_app/updateOrder',auth="public",type="json",method="PUT")
    def updateOrder(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.order_model"].sudo().search(domain)
            updated = cat.sudo().write(response)
            if (updated):
                data = {  "status":200, "result":cat.id }
            else:
                data = { "status":400, "result":"Order not modified"}
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #DELETE A order
    @http.route('/bar_app/deleteOrder',auth="public",type="json",method="DELETE")
    def deleteOrder(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.order_model"].sudo().search(domain).unlink()
            data = {  "status":200, "result":"Order deleted" }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data


    #############################################################
    ####################### PRODUCT MODEL ########################
    #############################################################
    #GET one product by id
    @http.route('/bar_app/getProduct/<int:catid>',auth="public",type="http")
    def getProduct(self,catid=None,**kw):
        if catid:
            domain = [("id","=",catid)]
        else:
            domain = []
        taskdata = http.request.env["bar_app.product_model"].sudo().search_read(domain,["name","price","description","category","ingredients"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #GET all product
    @http.route('/bar_app/getProducts',auth="public",type="http")
    def getProducts(self,**kw):
        taskdata = http.request.env["bar_app.product_model"].sudo().search_read([],["name","price","description","category","ingredients"])
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #POST ine product
    @http.route('/bar_app/addProduct',auth="public",type="json",method="POST")
    def addProduct(self,**kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.product_model"].sudo().create(response)
            data = {  "status":201, "id":result.id  }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #UPDATE one product
    @http.route('/bar_app/updateProduct',auth="public",type="json",method="PUT")
    def updateProduct(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.product_model"].sudo().search(domain)
            updated = cat.sudo().write(response)
            if (updated):
                data = {  "status":200, "result":cat.id }
            else:
                data = { "status":400, "result":"Product not modified"}
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #DELETE A product
    @http.route('/bar_app/deleteProduct',auth="public",type="json",method="DELETE")
    def deleteProduct(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.product_model"].sudo().search(domain).unlink()
            data = {  "status":200, "result":"Product deleted" }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #############################################################
    ####################### INVOICE MODEL #######################
    #############################################################
    #GET one invoice by id
    @http.route('/bar_app/getInvoice/<int:catid>',auth="public",type="http")
    def getInvoice(self,catid=None,**kw):
        if catid:
            domain = [("id","=",catid)]
        else:
            domain = []
        taskdata = http.request.env["bar_app.invoice_model"].sudo().search_read(domain,["ref","client","lines","base","vat","total","creationDate","state"])
        for t in taskdata:
            t['creationDate'] = t['creationDate'].isoformat()
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #GET all invoice
    @http.route('/bar_app/getInvoices',auth="public",type="http")
    def getInvoices(self,**kw):
        taskdata = http.request.env["bar_app.invoice_model"].sudo().search_read([],["ref","client","lines","base","vat","total","creationDate","state"])
        for t in taskdata:
            t['creationDate'] = t['creationDate'].isoformat()
        data = { "status":200, "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    #UPDATE one invoice
    @http.route('/bar_app/updateInvoice',auth="public",type="json",method="PUT")
    def updateInvoice(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.invoice_model"].sudo().search(domain)
            updated = cat.sudo().write(response)
            if (updated):
                data = {  "status":200, "result":cat.id }
            else:
                data = { "status":400, "result":"Invoice not modified"}
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #DELETE A invoice
    @http.route('/bar_app/deleteInvoice',auth="public",type="json",method="DELETE")
    def deleteInvoice(self,**kw):
        response = request.jsonrequest
        domain = [("id","=",response["id"])]
        try:
            cat = http.request.env["bar_app.invoice_model"].sudo().search(domain).unlink()
            data = {  "status":200, "result":"Invoice deleted" }
            return data
        except Exception as e:
            data = { "status":404, "error":e}
            return data

    #############################################################
    ################ INVOICE AUTOMATIC CREATION #################
    #############################################################
    @http.route('/bar_app/confirmOrder/<int:catid>',auth="public",type="http")
    def confirmOrder(self,catid=None,**kw):
        if catid:
            domain = [("id","=",catid)]
        else:
            domain = []
        order = http.request.env["bar_app.order_model"].sudo().search(domain)
        data = { "status":200, "stateOrder":order.changeState()}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")