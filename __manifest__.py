# -*- coding: utf-8 -*-
{
    'name': "jt_product_attribute_css",

    'summary': "Add support for dual color and css attributes",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_attribute_views.xml',
        'views/sale_variant_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        'web.assets_common': [
            'jt_product_attribute_css/static/src/scss/*',
        ],
    },       
}
