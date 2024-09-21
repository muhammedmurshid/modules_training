from odoo import models, api, _, fields


class ModulesTraining(models.Model):
    _name = "logic.modules.training"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'department_id'
    _description = 'Training Session'

    department_id = fields.Many2one('hr.department', string="Department")
    training_ids = fields.One2many('training.sessions', 'training_id', string="Trainings")
    head_id = fields.Many2one('hr.employee', string="Head", related='department_id.manager_id')
    mode = fields.Selection(
        [('by_company', 'By Company'), ('by_department', 'By Department'), ('by_employee', 'By Employee')],
        string='Mode', default='by_department')
    employee_id = fields.Many2one('hr.employee', string="Employee")
    company_id = fields.Many2one('res.company', string="Company",
                                  default=lambda self: self.env.company.id)
    name = fields.Text(string='Name')

    # def raineffect(self):
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'celebration_button',  # Custom tag for JS action
    #     }

    @api.onchange('mode')
    def _onchange_mode(self):
        if self.mode == 'by_department':
            self.employee_id = False
            self.company_id = False
        if self.mode == 'by_employee':
            self.company_id = False
            self.department_id = False
        if self.mode == 'by_company':
            self.employee_id = False
            self.department_id = False

class TrainingSessions(models.Model):
    _name = "training.sessions"

    description = fields.Text(string="Description")
    sessions = fields.Binary(string="Sessions")
    training_id = fields.Many2one('logic.modules.training', ondelete='restrict')
