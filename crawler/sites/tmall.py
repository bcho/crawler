# coding: utf-8

from brownant import Site
from requests import Session

from crawler.utils import custom_headers
from crawler.parsers import detail_m_tmall, site_m_tmall
from crawler.models import queue, item
from crawler.core.loggings import logger


site = Site(name='tmall')
http = Session()


@site.route('detail.m.tmall.com', '/item.htm')
def tmall_item(request):
    url = request.url.geturl()
    logger.debug('Fetching {0}.'.format(url))
    content = http.get(url, headers=custom_headers).content

    item_infos = detail_m_tmall.parse(content)
    item_infos.update({
        'id': request.args['id']
    })
    queue.resolve_one(url)
    logger.debug('Fetched {0} {1}.'.format(url, item_infos['id']))

    item.store(item_infos)

    return item_infos


@site.route('<name>.m.tmall.com', '/')
def tmall_index(request, name):
    url = request.url.geturl()
    logger.debug('Fetching {0}'.format(url))
    content = http.get(url, headers=custom_headers).content

    cates = site_m_tmall.parse_categories(content)
    queue.resolve_one(url)
    logger.debug('Fetched {0} {1}'.format(url, len(cates)))

    unparsed_cate_urls = [u for _, u in cates if not queue.exists(u)]
    queue.create_many(unparsed_cate_urls)

    return {
        'name': name,
        'categories': cates
    }


@site.route('<name>.m.tmall.com', '/shop/shop_auction_search.htm')
def tmall_category(request, name):
    # TODO multiple pages
    url = request.url.geturl()
    logger.debug('Fetching {0}'.format(url))
    content = http.get(url, headers=custom_headers).content

    items = site_m_tmall.parse_items(content)
    queue.resolve_one(url)
    logger.debug('Fetched {0} {1}'.format(url, len(items)))

    unparsed_item_urls = [u for u in items if not queue.exists(u)]
    queue.create_many(unparsed_item_urls)

    return {
        'name': name,
        'scid': request.args.get('scid'),
        'items': items
    }
