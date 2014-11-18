from __future__ import division
from collections import defaultdict
from heapq import nlargest
import math
import numpy as np


def compute(texts):
    N = len(texts)
    score = defaultdict(lambda : list([0.] * N))
    # word count
    for i, text in enumerate(texts):
        for word in text:
            score[word][i] += 1
    words = score.keys()

    # normalize: tf
    M = np.array(score.values())
    for j in range(N):
        M[:,j] /= max(M[:,j])

    # tf-idf
    for row in M:
        n = sum(row != 0)
        idf = math.log(N / n, 2)
        row *= idf

    return M, words


def topn(M, words, titles, n):
    for j in range(M.shape[1]):
        doc = M[:,j]
        print 'Title:', titles[j]
        l = [(val, i) for i, val in enumerate(doc)]
        for val, i in nlargest(n, l):
            print '%s: %s' % (words[i], val)
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

    M, words = compute(texts)
    topn(M, words, titles, 5)
