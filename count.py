import heapq
from collections import defaultdict


def count(iterable):
    count = defaultdict(int)
    for item in iterable:
        count[item] += 1
    return count


def nlargest(wc, n):
    return heapq.nlargest(n, wc.iteritems(), lambda (item, cnt): cnt)


top10 = lambda iterable: nlargest(iterable, 10)



def test():
    from book import text2 as text
    from ngram import bigram, trigram
    from stop import remove

    print 'word count top10:'
    print top10(count(remove(text)))

    print 'bigram top10:'
    print top10(count(bigram(remove(text))))

    print 'trigram top10:'
    print top10(count(trigram(remove(text))))


if __name__ == '__main__':
    test()
