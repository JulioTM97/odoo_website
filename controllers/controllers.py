# -*- coding: utf-8 -*-
from odoo import http
from odoo import models
from odoo.exceptions import UserError

class WebsiteTest(http.Controller):
    @http.route('/website_test', auth='public', website=True)
    def index(self, **kw):
        Xelementor = http.request.env['webtest']
        return http.request.render('website_test.index', {
            'Yelementor': Xelementor.search([])
        })

    @http.route('/website_test/<model("webtest"):elemento>/', auth='public', website=True)
    def elemento(self,elemento):
        return http.request.render('website_test.peace_sign', {
            'asunto':elemento
        })        

    @http.route('/blogpost/comment', type='http', auth="public", website=True)
    def insertar(self, **post):
        registro = http.request.env['webtest'].create({'name': post['name'], 'description' : post['description']})
        return self.index()