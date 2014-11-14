def ngram(text, n):
    grams = []
    for word in text:
        grams.append(word)
        if len(grams) == n:
            yield tuple(grams)
            grams.pop(0)


bigram = lambda text: ngram(text, 2)
trigram = lambda text: ngram(text, 3)


def test(text):
    print '-' * 40
    print 'text:', text
    print

    print 'bi-grams:'
    for item in bigram(text):
        print item
    print

    print 'tri-grams:'
    for item in trigram(text):
        print item
    print

    print '5-grams:'
    for item in ngram(text, 5):
        print item


if __name__ == '__main__':
    from book import sent1, text1
    test(sent1)
    test(text1[:30])
