from __future__ import print_function
import string
from nltk.corpus import stopwords

from framework import run

stops = set(stopwords.words('english')) | set(string.punctuation)

def wcmap(text):
    wc = []
    for word in text:
        w = word.lower()
        if w not in stops:
            wc.append((w, 1))
    return wc

def wcreduce(word, counts):
    return word, sum(counts)


from book import text1
for word, count in run(text1*1000, wcmap, wcreduce):
    print(word, count)
