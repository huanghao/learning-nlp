from __future__ import division
from collections import defaultdict
from heapq import nlargest
import math

from count import count


def tfidf(*texts):
    tfs = []
    for text in texts:
        wc = count(text)
        max_freq = max(wc.values())
        tf = {word: (cnt/max_freq) for word, cnt in wc.iteritems()}
        tfs.append(tf)

    idf = defaultdict(int)
    for tf in tfs:
        for word in tf:
            idf[word] += 1

    N = len(texts)
    idf = {word: math.log(N/n, 2) for word, n in idf.items()}

    return [{word: (tf_ * idf[word]) for word, tf_ in tf.iteritems()}
        for tf in tfs]


def top(tfidf, n):
    for i, scores in enumerate(tfidf):
        top = nlargest(n, scores.iteritems(), key=lambda (word, score): score)
        print 'Top %d words that could identify text%d:' % (n, i+1)
        for word, score in top:
            print '%s: %f' % (word, score)
        print


if __name__ == '__main__':
    from book import *
    from stop import remove, lower
    texts = [lower(remove(t)) for t in
        (text1, text2, text3, text4, text5, text6, text7, text8, text9)]
    
    top(tfidf(*texts), 5)
