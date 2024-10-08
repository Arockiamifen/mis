# -*- coding: utf-8 -*-

{
    'name': 'Educational Exam Management MIS',
    'version': '17.0.1.0.1',
    'category': 'Industries',
    'summary': """Sneak the Examination Management in Educational ERP""",
    'description': """An easy way to handle the examinations in an educational 
     system with better reports and exam valuation and exam result facilities""",
    'author': 'Alanniainfotechz',
    'company': 'Alanniainfotechz',
    'maintainer': 'Alanniainfotechz',
    'depends': ['mis_education_core'],
    'data': [
        'security/ir.model.access.csv',
        'views/education_exam_views.xml',
        'views/education_exam_valuation_views.xml',
        'views/education_exam_results_views.xml',
        'views/education_student_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
