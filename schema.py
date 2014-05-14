# coding: utf-8

'''
    schema
    ~~~~~~

    Initiate crawler's database schema.
'''

from crawler import app as app_builder
from crawler.core.database import db
from crawler.core.loggings import logger


app_builder.build()


schema = '''
CREATE TABLE `queue` (
    `id` INTEGER PRIMARY KEY,
    `url` TEXT,
    `resolved` INTEGER DEFAULT 0
);
'''

db.get_cursor().execute(schema)
logger.info('Schema built.')
