"""
- lower case
- strip HTML tags
- normalize URLs
- normalize Email addresses
- normalize numbers
- normalize dollars
- word stemming
- remove non-words

$ python process_email.py CSDMC2010_SPAM/TESTING.body/TEST_00003.eml
spam dear emailaddr number numberff ..
"""
import re
import sys
import string

from nltk import PorterStemmer


TAG = re.compile(r'<.*?>')
EMAIL = re.compile(r'\S+@\S+')
NUM = re.compile(r'\d+')
URL = re.compile(r'(http|https)://\S*')
PU = re.compile('[' + string.punctuation + ']')


def preprocess(text):
    """
    Assume that text is unicode type
    """
    text = text.lower()
    text = TAG.sub('', text)
    text = EMAIL.sub('emailaddr', text)
    text = NUM.sub('number', text)
    text = URL.sub('httpaddr', text)
    text = text.replace('$', 'dollar')
    text = PU.sub(' ', text)

    porter = PorterStemmer()
    for word in text.split():
        yield porter.stem(word)


if __name__ == '__main__':
    for word in preprocess(open(sys.argv[1]).read()):
        print word,
    print
