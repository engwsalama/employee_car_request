# -*- coding: utf-8 -*-
from odoo import http

# class EmployeeCar-request(http.Controller):
#     @http.route('/employee_car-request/employee_car-request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_car-request/employee_car-request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_car-request.listing', {
#             'root': '/employee_car-request/employee_car-request',
#             'objects': http.request.env['employee_car-request.employee_car-request'].search([]),
#         })

#     @http.route('/employee_car-request/employee_car-request/objects/<model("employee_car-request.employee_car-request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_car-request.object', {
#             'object': obj
#         })