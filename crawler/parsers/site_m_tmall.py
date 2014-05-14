# coding: utf-8

'''
    parsers.site_m_tmall
    ~~~~~~~~~~~~~~~~~~~~

    Parser for `<name>.m.tmall.com`
'''

import re

from lxml import html


ID_PATTERN = re.compile('^.*/i(\d+).htm.*$')
ITEM_DETAIL_URL_TMPL = 'http://detail.m.tmall.com/item.htm?id={0}'


def parse_categories(content):
    etree = html.fromstring(content)

    rv = []
    for node in etree.xpath('.//li[@class="node"]'):
        if 'data-url' in node.attrib:
            rv.append((node.text, node.attrib['data-url']))

    return rv


def parse_items(content):
    etree = html.fromstring(content)

    rv = []
    for item in etree.xpath('.//div[@class="block first"]/ul/li/a'):
        url = item.attrib['href']
        if ID_PATTERN.match(url):
            item_id = ID_PATTERN.findall(url)[0]
            rv.append(ITEM_DETAIL_URL_TMPL.format(item_id))

    return rv
