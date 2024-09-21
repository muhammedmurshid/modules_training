{
    'name': "Training",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'mail', 'logic_certificates', 'qualitative_analysis'],
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/training.xml',

    ],
    'assets': {
        'web.assets_backend': [
            '/modules_training/static/src/js/win_effect.js',
            '/modules_training/static/src/js/win_effect_trigger.js',
            'modules_training/static/src/css/confetti.css'],
    },
    'demo': [],
    'summary': "logic_modules_training",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}
