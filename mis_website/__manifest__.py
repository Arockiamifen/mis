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
    'depends': ['web','website','mis_school_management'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/web_menu_data.xml',
        'data/sequence.xml',
        'data/web_menu.xml',
        'views/program_gallery_view.xml',
        'views/web_info_view.xml',
        'views/web_video_view.xml',
        'views/mis_home_template.xml',
        'views/home_template.xml',
        'views/prospectus_template.xml',
        'views/academics_template.xml',
        'views/school_commitee_temp.xml',
        'views/program_and_events.xml',
        'views/online_application_templates.xml',
        'views/student_portal_templates.xml',
        # 'views/template.xml',
        'views/nav_bar_template.xml',
        'views/menu.xml',

    ],

    # 'assets': {
    #     'web.assets_backend': [
    #         '/mis_website/static/src/js/video_field.xml'
    #         '/mis_website/static/src/js/video_field.js'
    #     ],
    # },
    'assets': {
        'web.assets_frontend': [
            # '/mis_website/static/src/css/style.css',
            # '/mis_website/static/src/css/sample.css',
            # '/mis_website/static/src/js/online_application.js',
        ],
    },


    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
