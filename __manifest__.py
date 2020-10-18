# -*- coding: utf-8 -*-
{
    'name': "l10n_ar_account_portal_document",

    'summary': """
        Add document type to portal (Argentina)""",

    'description': """
        With this module you're able to create different memberships, the subscribers are allowed to select the sessions
        that they're going and check their billing.
    """,

    'author': "Miguel Hatrick",
    'website': "http://www.dacosys.com",

    'category': 'Events',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_ar_account'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}