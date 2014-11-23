import re
import requests
import requests_cache
from pyquery import PyQuery as pq

requests_cache.install_cache()


URL = re.compile(r'http://book.douban.com/subject/[^/]+')

def parse(url):
    print 'get', url, '..'
    html = requests.get(url).content.decode('utf8')
    div = pq(html).find('div#info')
    lines = pq(div).html().split('<br/>')
    items = [pq(l).text().strip().split(':', 1) for l in lines if l.strip() != '']
    urls = URL.findall(html)
    return items, urls


seed = 'http://book.douban.com/subject/3259440/'

visited = {}
queue = [seed]
times = 0
while queue and times < 50:
    url = queue.pop()
    if url in visited:
        continue
    meta, urls = parse(url)
    visited[url] = True
    for k, v in meta:
        print ('%s: %s' % (k, v)).encode('utf8')
    times += 1
    queue.extend(urls)
