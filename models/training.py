from odoo import models, api, _, fields

class ModulesTraining(models.Model):
    _name = "logic.modules.training"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'department_id'
    _description = 'Training Session'

    department_id = fields.Many2one('hr.department', string="Department")
    training_ids = fields.One2many('training.sessions', 'training_id', string="Trainings")
    head_id = fields.Many2one('hr.employee', string="Head", related='department_id.manager_id')


class TrainingSessions(models.Model):
    _name = "training.sessions"

    description = fields.Text(string="Description")
    sessions = fields.Binary(string="Sessions")
    training_id = fields.Many2one('logic.modules.training', ondelete='restrict')