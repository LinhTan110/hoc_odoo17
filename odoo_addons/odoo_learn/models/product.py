# __author__ = 'ITPLUS'



from odoo import models, fields, api
#from odoo.models import Model

class Product(models.Model):
    _name = 'learn.product' # learn_employee
    _description = 'Product information manager'

    name = fields.Char()
    description = fields.Text()
    price = fields.Integer()
    cost = fields.Integer()

    #fields.Integer()
    #fields.Float()
    #fields.Boolean()
    #fields.Datetime()
