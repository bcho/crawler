# coding: utf-8

'''
    crawler.models.queue
    ~~~~~~~~~~~~~~~~~~~~

    Work queue model defination.
'''

from crawler.core.database import db


__all__ = ['fetch_one', 'resolve_one', 'create_one', 'create_many', 'empty',
           'exists', 'has_unresolved_job']


def fetch_one():
    '''Get a job from queue.'''
    cur = db.get_cursor()
    cur.execute('SELECT `url` FROM `queue` WHERE `resolved` = 0 LIMIT 1')
    rv = cur.fetchone()

    if not rv:
        return
    return dict(url=rv[0])


def resolve_one(url):
    '''Mark a job as resolved.

    :param url: job's url.
    '''
    cur = db.get_cursor()
    cur.execute('UPDATE `queue` SET `resolved` = 1 WHERE `url` = ?',
                (url,))
    db.commit()


def _create_one(url, do_commit=False):
    '''Create a job.

    :param url: job's url
    :param do_commit: indicate whether commit change after insert. Defaults to
                      ``False``.
    '''
    cur = db.get_cursor()
    cur.execute('INSERT INTO `queue` (`url`) VALUES (?)', (url,))

    if do_commit:
        db.commit()


def create_one(url):
    '''Create a job.

    :param url: job's url.
    '''
    _create_one(url, do_commit=True)


def create_many(urls):
    '''Create some jobs.

    :param urls: jobs' urls.
    '''
    for url in urls:
        _create_one(url, do_commit=False)
    db.commit()


def exists(url):
    '''Check if a job exists.

    :param url: job's url
    '''
    cur = db.get_cursor()
    cur.execute('SELECT COUNT(*) FROM `queue` WHERE `url` = ?',
                (url,))
    rv = cur.fetchone()
    return rv[0] > 0


def empty():
    '''Empty jobs queue.'''
    cur = db.get_cursor()
    cur.execute('DELETE FROM `queue`')
    db.commit()


def has_unresolved_job():
    '''Check if there are unresolved jobs.'''
    cur = db.get_cursor()
    cur.execute('SELECT COUNT(*) FROM `queue` WHERE `resolved` = 0')
    rv = cur.fetchone()
    return rv[0] > 0
