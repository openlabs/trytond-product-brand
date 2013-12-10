# -*- coding: utf-8 -*-
"""
    __init__

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from brand import Brand, Template


def register():
    Pool.register(
        Brand,
        Template,
        module='product_brand', type_='model'
    )
