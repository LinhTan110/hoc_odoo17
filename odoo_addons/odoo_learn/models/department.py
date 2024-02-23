from odoo import fields, models, api


class Department(models.Model):
    _name = 'department'
    _description = 'Description'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    employee_ids = fields.One2many(
        comodel_name='learn.employee', inverse_name='department_id', string='Employee')