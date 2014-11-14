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


def top(tfidf, n, titles):
    for i, scores in enumerate(tfidf):
        top = nlargest(n, scores.iteritems(), key=lambda (word, score): score)
        print 'Top %d words that could identify text%d:' % (n, i+1)
        print titles[i]
        for word, score in top:
            print '%s: %f' % (word, score)
        print


if __name__ == '__main__':
    from book import *
    from stop import lower, remove_punctuation

    titles = '''text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
'''.splitlines()

    texts = [lower(remove_punctuation(t)) for t in
        (text1, text2, text3, text4, text5, text6, text7, text8, text9)]
    
    top(tfidf(*texts), 5, titles)
