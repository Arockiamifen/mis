# -*- coding: utf-8 -*-

{
    'name': ' School Education Management for MIS',
    'version': '17.0.1.0.1',
    'category': 'School',
    'summary': """This modules helps to manage the School MIS 
     education system""",
    'description': """This module serves as a comprehensive solution for
     efficiently managing the education system of a university enhancing
     its overall functionality and user experience.""",
    'author': 'Alannia Infotechz',
    'company': 'Alannia Infotechz',
    'maintainer': 'Alannia Infotechz',
    'depends': ['base' , 'mail', 'hr'],
    'data': [
        # 'security/security_groups.xml',
        'security/ir.model.access.csv',
        # 'data/ir_sequence_data.xml',
        # 'data/mail_template_data.xml',

        'views/mis_student_view.xml',
        'views/mis_academic_year_view.xml',
        'views/mis_teacher_view.xml',
        'views/mis_subject_view.xml',
        'views/mis_class_view.xml',
        'views/menu.xml',
    ],
    # 'assets': {
    #     'web.assets_frontend': [
    #         '/mis_school_management/static/src/css/web_style.css',
    #         '/mis_school_management/static/src/js/online_application.js'
    #     ],
    # },
    'images': ['static/description/schoolnew.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
