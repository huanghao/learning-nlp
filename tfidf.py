from __future__ import division
from collections import defaultdict
from heapq import nlargest
import math


def compute(texts):
    N = len(texts)
    score = defaultdict(lambda : list([0] * N))
    # word count
    for i, text in enumerate(texts):
        for word in text:
            score[word][i] += 1

    # max word count in doc[i]
    maxs = [0] * N
    for word, counts in score.iteritems():
        for i, cnt in enumerate(counts):
            maxs[i] = max(maxs[i], cnt)

    # standardize: tf
    for word, counts in score.iteritems():
        for i in range(N):
            counts[i] /= maxs[i]

    # tf-idf
    for word, tf in score.iteritems():
        n = sum(bool(i) for i in tf)
        idf = math.log(N / n, 2)
        for i in range(N):
            tf[i] *= idf

    return score


def to_docs(score):
    N = len(score.itervalues().next())
    docs = [list() for _ in range(N)]

    for word, tfidf in score.iteritems():
        for i, val in enumerate(tfidf):
            if val > 0:
                docs[i].append((val, word))
    return docs


def topn(docs, titles, n):
    for i, doc in enumerate(docs):
        print 'Title:', titles[i]
        for val, word in nlargest(n, doc):
            print '%s: %s' % (word, val)
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
    texts = (text1, text2, text3, text4, text5, text6, text7, text8, text9)
    texts = [lower(remove_punctuation(t)) for t in texts]

    score = compute(texts)
    docs = to_docs(score)
    topn(docs, titles, 5)
