# Defined by user
import string
from nltk.corpus import stopwords

stops = set(stopwords.words('english')) | set(string.punctuation)

def wcmap(text):
    for word in text:
        w = word.lower()
        if w not in stops:
            yield w, 1

def wcreduce(word, counts):
    return word, sum(counts)


# Defined by frameword
from collections import defaultdict

def split(text, chunks):
    total = len(text)
    sz = total / chunks
    for i in range(0, total, sz):
        yield text[i:i+sz]

def run(data, mapf, reducef, chunks=10, mconcurrency=3, rconcurrency=3):
    groups = defaultdict(list)

    for chunk in split(data, chunks):
        # runs in parrallel
        for k, v in mapf(chunk):
            groups[k].append(v)

    for k, values in groups.iteritems():
        # runs in parrallel
        yield reducef(k, values)


from book import text1
for word, count in run(text1, wcmap, wcreduce):
    print word, count
