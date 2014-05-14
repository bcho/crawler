# coding: utf-8

'''
    core.database
    ~~~~~~~~~~~~~

    Simple sqlite3 database wrapper.
'''

import sqlite3
import logging


class Store(object):

    #: Connection string.
    CONNECTION_STRING = ':memory:'

    #: Logger instance.
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.conn = None

    @classmethod
    def configure(cls, conn_str, logger=None):
        '''Configure sql connection.

        :param conn_str: connection string.
        :param logger: logger instance. Defaults to current module's logger.
        '''
        cls.CONNECTION_STRING = conn_str
        if logger:
            cls.logger

    def get_cursor(self):
        '''Get a cursor instance.'''
        if self.conn is None:
            self._connect()

        return self.conn.cursor()

    def commit(self):
        '''Commit changes.'''
        if self.conn is None:
            return

        self.conn.commit()

    def _connect(self):
        '''Connection to database.'''
        conn_str = self.CONNECTION_STRING
        self.logger.info('Create connection to database: {0}'.format(conn_str))
        self.conn = sqlite3.connect(conn_str)

    def __del__(self):
        '''Close connection on object delete.'''
        if self.conn is not None:
            self.conn.close()
            self.logger.info('Close connection.')


db = Store()
