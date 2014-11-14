import string
from itertools import ifilter, imap

from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))
punctuation = set(string.punctuation)

not_a_stop_word = lambda i: i not in stopwords
not_a_punctuation = lambda i: i not in punctuation
norm = lambda i: not_a_stop_word(i) and not_a_punctuation(i)

remove_stop_words = lambda text: ifilter(not_a_stop_word, text)
remove_punctuation = lambda text: ifilter(not_a_punctuation, text)
remove = lambda text: ifilter(norm, text)

lower = lambda text: imap(str.lower, text)


def test(text):
    print 'text:', text

    print 'remove stop words:'
    print list(remove_stop_words(text))

    print 'remove punctuation:'
    print list(remove_punctuation(text))

    print 'remove all:'
    print list(remove(text))


if __name__ == '__main__':
    from book import sent1, text1
    test(sent1)
    test(text1[:50])
