# -*- coding: utf-8 -*-
"""
    Brands Module for Tryton

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta

__all__ = ['Brand', 'Template']
__metaclass__ = PoolMeta


class Brand(ModelSQL, ModelView):
    "Product Brand"
    __name__ = "product.brand"

    name = fields.Char('Name', size=None, required=True, translate=True)
    notes = fields.Text('Brand Notes')
    product_templates = fields.One2Many(
        'product.template', 'brand', 'Products'
    )


class Template:
    "Product Template"
    __name__ = "product.template"

    #Only here because a o2m always has a corresponding m2o
    brand = fields.Many2One(
        'product.brand', 'Product Brand'
    )
