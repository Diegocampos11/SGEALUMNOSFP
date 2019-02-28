# -*- coding: utf-8 -*-
from odoo import http

# class Alumnosfp(http.Controller):
#     @http.route('/alumnosfp/alumnosfp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alumnosfp/alumnosfp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alumnosfp.listing', {
#             'root': '/alumnosfp/alumnosfp',
#             'objects': http.request.env['alumnosfp.alumnosfp'].search([]),
#         })

#     @http.route('/alumnosfp/alumnosfp/objects/<model("alumnosfp.alumnosfp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alumnosfp.object', {
#             'object': obj
#         })