# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cetak Kwitansi',
    'version': '12.0.0.0',
    'category': 'Account',
    'summary': 'Mencetak kwitansi pembayaran.',
    'description': """
    Mencetak kwitansi pembayaran (Menu Accounting,Customer,Payment).


    
""",
    'price': 000,
    'currency': 'USD',
    'author': 'fikrisoftware',
    'website': 'https://odoo.fik-soft.com',
    'depends': ['base','account'],
    'data': [
            'views/keterangan.xml',
            'report/kwitansi.xml',
            'report/kwitansi_doc.xml',
    ],
    'installable': True,
    'application':True, 
    'auto_install': False,
    "images":["static/description/hasil.png"],
}

