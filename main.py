# coding: utf-8

from crawler import app as app_builder
from crawler.models import queue


app = app_builder.build()

queue.empty()

queue.create_one('http://hegou.m.tmall.com')
while queue.has_unresolved_job():
    url = queue.fetch_one()['url']
    app.dispatch_url(url)
