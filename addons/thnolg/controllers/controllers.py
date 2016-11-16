# -*- coding: utf-8 -*-
from odoo import http

# class Thnolg(http.Controller):
#     @http.route('/thnolg/thnolg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thnolg/thnolg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('thnolg.listing', {
#             'root': '/thnolg/thnolg',
#             'objects': http.request.env['thnolg.thnolg'].search([]),
#         })

#     @http.route('/thnolg/thnolg/objects/<model("thnolg.thnolg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thnolg.object', {
#             'object': obj
#         })