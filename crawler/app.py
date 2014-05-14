# coding: utf-8

from brownant import Brownant


def setup_sites(app):
    from crawler.sites import tmall

    app.mount_site(tmall.site)


def setup_configs(default_config_module):
    from crawler.core.config import Config

    config = Config()
    config.from_object(default_config_module)
    config.from_environ('CRAWLER_CONF', silent=True)

    return config


def setup_loggers(config):
    from crawler.core import loggings

    loggings.configure(config)


def setup_database(config):
    from crawler.core.loggings import logger
    from crawler.core.database import db

    db.configure(config['DATABASE_CONNECTION'], logger)


def build(**extra_configs):
    config = setup_configs('crawler.configs.default')

    setup_loggers(config)
    setup_database(config)

    app = Brownant()
    setup_sites(app)

    return app
