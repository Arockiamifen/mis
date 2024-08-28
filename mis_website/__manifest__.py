# -*- coding: utf-8 -*-

{
    'name': ' MIS School Education Management',
    'version': '17.0',
    'category': 'School',
    'summary': """Manage the MIS School Website education system""",
    'description': """This modules helps to organize the website data and helps to update the website datas""",
    'author': 'Alannia',
    'company': 'alanniainfotechz',
    'maintainer': 'Alanniainfotechz',
    'depends': ['website','mis_school_management'],
    'data': [
        # 'security/ir.model.access.csv',
        'data/web_menu_data.xml',
        'views/online_application_templates.xml',
        'views/student_portal_templates.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            '/mis_website/static/src/css/web_style.css',
            '/mis_website/static/src/js/online_application.js'
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
