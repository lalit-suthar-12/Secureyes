# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Travel Management',
    'version' : '1.0',
    'summary': 'Travel Management',
    'description': """travelling services""",
    'category': 'Productivity',
    'website': 'secureyes.net',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/createtrip.xml',
        'views/trl.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
