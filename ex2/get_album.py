import re
import sys
import json

import requests
import requests_cache
from pyquery import PyQuery as pq

requests_cache.install_cache()

def parse_album(url):
    url = 'http://music.baidu.com%s' % url
    html = pq(requests.get(url).content)
    title = html.find('h2.album-name').text().encode('utf8')
    singer = html.find('span.author_list').text().encode('utf8')
    info = html.find('li.album-singer').next('li').text().encode('utf8')
    print '<%s> - %s\t\t%s' % (title, singer, info)
    return other_albums(html)


def other_links(html):
    links = {
        'album': set(),
        'artist': set(),
        }
    for a in html.find('a'):
        href = pq(a).attr('href') or ''
        m = re.match(r'(/(album|artist)/\d+)', href)
        if m:
            links[m.gropu(2)].add(m.group(1))
    return links


if len(sys.argv) > 1:
    seed = sys.argv[1]
else:
    seed = '/album/124269789'

visited = set()
queue = [seed]

i = 0
while i < 100 and queue:
    url = queue.pop()
    if url in visited:
        continue
    visited.add(url)
    i += 1
    links = 
    queue.extend(get_info(album))
