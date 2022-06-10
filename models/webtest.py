# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class website_test(models.Model):
    _name = 'webtest'
    _description = 'this model/table is about a website module test.'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()
    comentario = fields.Html()

    def action_create_record(self,valores):
        raise UserError (str(type(valores))+"\n"+str(valores))

