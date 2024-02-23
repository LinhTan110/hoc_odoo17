# __author__ = 'ITPLUS'



from odoo import models, fields, api
#from odoo.models import Model

class Employee(models.Model):
    _name = 'learn.employee' # learn_employee
    _description = 'Employee information manager'

    name = fields.Char(string='Name', required=True)
    dob = fields.Date(string='Birthday')
    phone = fields.Char(string='Phone', required=1)
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')
    company = fields.Char(string='Company', default='Cong ty TNHH')
    gender = fields.Selection(string='Gender',
                              selection=[('male', 'Male'), ('female', 'Female')])
    department_id = fields.Many2one(comodel_name='department', string='Department')

    #fields.Integer()
    #fields.Float()
    #fields.Boolean()
    #fields.Datetime()
