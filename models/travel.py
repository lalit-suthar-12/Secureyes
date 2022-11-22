from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError



class TrManagement(models.Model):
    _name = "travel.customer"
    _description = "Travel Management"

    name = fields.Char(string='Employee Name', required=True)
    manager_name = fields.Char(string="Manager Name", required=True)
    note = fields.Text(string='Description')
    employee_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender", default='order')
    job_role = fields.Selection([
        ('full stack developer', 'Full Stack Developer'),
        ('web developer', 'Web Developer'),
        ('python developer', 'Python Developer'),
        ('c# developer', 'C# Developer'),
        ('java developer', 'Java Developer')
    ], string="Job Role", required=True)

    department = fields.Selection([
        ('hr', 'HR'),
        ('it', 'IT'),
        ('sales', 'Sales'),
        ('purchase', 'Purchase'),
    ], string="Department", required=True)

    destination = fields.Char(string="Destination", required=True)
    departure = fields.Char(string="Departure", required=True)
    train_name = fields.Char(string="Train Name", required=True)
    train_number = fields.Char(string="Train No.", required=True)
    number_of_days = fields.Char(string="Number of Days", required=True)
    arrival_date = fields.Datetime(string="Arrival Date")
    return_date = fields.Date(string="Return Date")
    responsible_id = fields.Text(string="Customer")
    one2many_ids = fields.One2many('travel.customer1', 'field1', string='O2M')
    tags_ids = fields.Many2many('res.partner.category', string="Tags")

    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    currency_id = fields.Many2one('res.currency', string="Currency")
    salary = fields.Monetary(string="Salary")
    fees = fields.Float(string="Total Fees")

    is_intern = fields.Boolean(string="Is Intern")
    prescription = fields.Html(string="Prescription")
    future_date = fields.Date(string="Future Date")
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)

    state = fields.Selection([
        ('progress', 'Progress'),
        ('requested', 'Requested'),
        ('closed', 'Closed'),
        ('draft', 'Draft'),
    ], string="Status", default='draft')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    @api.onchange('future_date')
    def onchange_future_date(self):
        if self.future_date and self.future_date < date.today():
            raise ValidationError("Please select next date")

    def action_progress(self):
        for rec in self:
            rec.state = 'progress'

    def action_requested(self):
        for rec in self:
            rec.state = 'requested'

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'


class TrManagement1(models.Model):
    _name = "travel.customer1"
    _description = "Travel Management Description"

    task = fields.Char(string='Task', required=True)
    percentage = fields.Integer(string='% Completed')
    field1 = fields.Many2one('travel.customer', string='Field')
class TrManagement2(models.Model):
    _name = "travel.customer2"
    _description = "Travel Management Details"

    first_name = fields.Char(string="Employee First Name", required=True)
    second_name = fields.Char(string="Employee Second Name", required=True)
    employee_image = fields.Image(string='Employee Inage', max_width=100, max_height=100)
