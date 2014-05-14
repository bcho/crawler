# coding: utf-8

'''
    parsers.detail_m_tmall
    ~~~~~~~~~~~~~~~~~~~~~~

    Parser for `detail.m.tmall.com`
'''

import re

from lxml import html


SIZE_PATTERN = re.compile('\d+.*\*\d+.*')


def parse(content):
    etree = html.fromstring(content)

    return {
        'name': extract_name(etree),
        'price': extract_price(etree),
        'sales': extract_sales(etree),
        'size': extract_size(etree),
        'sku': extract_sku(etree)
    }


def extract_name(tree):
    name = tree.xpath('.//div[@class="title"]/h1')
    if name:
        name = name[0].text.strip()
    else:
        name = None

    return name


def extract_price(tree):
    price = tree.xpath('.//b[@class="p-price-v"]')
    if price:
        price = price[0].text
        if '-' in price:
            min_, max_ = price.split('-')
            price = dict(min=float(min_), max=float(max_))
        else:
            price = float(price)
    else:
        price = None

    return price


def extract_sales(tree):
    sales = tree.xpath('.//div[@class="m-sales"]/div[@class="value"]/b')
    if sales:
        sales = int(sales[0].text)
    else:
        sales = None

    return sales


def extract_sku(tree):
    return [i.text for i in tree.xpath('.//div[@class="items"]/label')]


def extract_size(tree):
    candidates = [i.text for i in tree.xpath('.//div[@class="items"]/label')]

    rv = []
    for candidate in candidates:
        if SIZE_PATTERN.match(candidate):
            rv.append(candidate)

    return rv
