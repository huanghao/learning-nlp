from __future__ import division


def jaccard(s, t):
    return len(s & t) / len(s | t)


def k_shingle(string, k):
    length = len(string)
    if length < k:
        return set()

    def shingles():
        start, end = 0, k
        while end <= length:
            yield string[start:end]
            start += 1
            end += 1

    return set(shingles())


def test(string):
    print 'string:', string

    for s in k_shingle(string, 4):
        print s

    
if __name__ == '__main__':
    from book import sent1, text1, text2, text3
    test(' '.join(sent1))

    feature1 = k_shingle(' '.join(text1), 5)
    feature2 = k_shingle(' '.join(text2), 5)
    feature3 = k_shingle(' '.join(text3), 5)
    print 'SIM(text1, text1) = ', jaccard(feature1, feature1)
    print 'SIM(text1, text2) = ', jaccard(feature1, feature2)
    print 'SIM(text1, text3) = ', jaccard(feature1, feature3)
    print 'SIM(text2, text3) = ', jaccard(feature2, feature3)
