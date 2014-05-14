# coding: utf-8

'''
    crawler.configs.default
    ~~~~~~~~~~~~~~~~~~~~~~~

    Default configurations for crawler.
'''

from os import path
base_dir = path.dirname(path.dirname(path.abspath(__file__)))
data_dir = path.join(path.dirname(base_dir), 'data')


#: Database connection string.
DATABASE_CONNECTION = path.join(data_dir, 'data.sqlite3')

#: Loggings
_delim = '-' * 80
LOGGING_FORMAT = _delim + '''
%(name)s:%(levelname)s %(asctime)s [%(pathname)s:%(lineno)d]:
%(message)s
''' + _delim
LOGGING_FILE = '/tmp/crawler.log'
