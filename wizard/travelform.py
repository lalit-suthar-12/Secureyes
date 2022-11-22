from odoo import api, fields, models

class CreateTrip(models.TransientModel):
    _name = "create.trip.wizard"
    _description = "Create trip wizard"

    city = fields.Char(string='City', required=True)
    # manager_name = fields.Char(string="Manager Name", required=True)
    note = fields.Text(string='Description')

    def action_create_trip(self):
        print("Your trip is planned")