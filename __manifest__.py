# -*- coding: utf-8 -*-
{
    'name': "Website_Test",
    'summary': "web test resumen",
    'description': "web test description",
    'author': "My Company",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','website'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/webtest_view.xml',
        'templates/main_template.xml',
    ],
}
