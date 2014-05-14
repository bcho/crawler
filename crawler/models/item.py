# coding: utf-8

'''
    crawler.models.item
    ~~~~~~~~~~~~~~~~~~~

    Item model defination.
'''

import json


__all__ = ['store']


def store(infos):
    '''Store a item record.'''

    with open('./data/{id}.json'.format(**infos), 'w') as f:
        f.write(json.dumps(infos, indent=4))
