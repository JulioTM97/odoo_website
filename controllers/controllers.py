# -*- coding: utf-8 -*-
from odoo import http

class WebsiteTest(http.Controller):

    @http.route('/website_test', auth='public', website=True)
    #Todos los parametros que se pasen seran almacenados en "**kw"
    #en este caso no se estan pasando parametros a esta funcion.
    def index(self, **kw):
        #Esta es la forma de crear un objeto del modelo "webtest"
        Xelementor = http.request.env['webtest']
        #Lo siguiente me va a mostrar el template de ID "index" alojado en el modulo "website_test"
        #Y le paso el parametro "Yelementor", que contiene los registros del modelo "webtest"
        return http.request.render('website_test.index', {'Yelementor': Xelementor.search([]) })



    #en la siguiente ruta, cuando se acceda a /website_test/[algo], si "algo" es un id de un modelo
    #se ejecutara la siguiente funcion.
    @http.route('/website_test/<model("webtest"):elemento>/', auth='public', website=True)
    #"elemento" es el registro que le pase por la url
    def elemento(self,elemento):
        #Lo siguiente me va a mostrar el template con el ID "peace_sign" alojado en el modulo "website_test"
        #Y le paso el parametro "asunto", que contendra el modelo que ha sido pasado por la url.
        return http.request.render('website_test.peace_sign', {'asunto':elemento})  



    @http.route('/blogpost/comment', type='http', auth="public", website=True)
    #"**post" tendra el valor de todos los parametros que se estan pasando por el metodo GET
    def insertar(self, **post):
        #Se crea un registro del modelo "webtest" con los datos almacenados en "post"
        registro = http.request.env['webtest'].create({'name': post['name'], 'description' : post['description']})
        return self.index()