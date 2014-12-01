from __future__ import print_function
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor as Executor


def split(text, chunks):
    total = len(text)
    sz = total / chunks
    for i in range(0, total, sz):
        yield text[i:i+sz]


def run(data, mapf, reducef, chunks=10, mconcurrency=3, rconcurrency=3):
    groups = defaultdict(list)

    with Executor(max_workers=mconcurrency) as ex:
        for kvs in ex.map(mapf, split(data, chunks)):
            for k, v in kvs:
                groups[k].append(v)

    with Executor(max_workers=rconcurrency) as ex:
        res = []
        for k, values in groups.iteritems():
            res.append(ex.submit(reducef, k, values))
        for f in res:
            yield f.result()
