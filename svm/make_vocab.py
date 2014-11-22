"""
$ python make_vocab.py CSDMC2010_SPAM/TRAINING.body > vocab.txt
..
$ wc -l vocab.txt
    1566 vocab.txt
$ head -2 vocab.txt
1 china
2 music
"""
import os
import sys
import logging
from collections import defaultdict

from process_email import preprocess


def make_vocabulary(token_stream, threshold=100):
    wc = defaultdict(int)
    for token in token_stream:
        wc[token] += 1
    tid = 1
    for token, cnt in wc.iteritems():
        if cnt >= threshold:
            yield tid, token
            tid += 1


def walk_emails(top):
    for dirname, dirnames, filenames in os.walk(top):
        for filename in filenames:
            if filename.endswith('.eml'):
                fname = os.path.join(dirname, filename)
                with open(fname) as file:
                    content = file.read()
                yield fname, content.decode('utf8', 'ignore')


def load_tokens(top):
    for fname, content in walk_emails(top):
        logging.debug('processing %s ..', fname)
        for token in preprocess(content):
            yield token


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    stream = load_tokens(sys.argv[1])
    for tid, token in make_vocabulary(stream):
        print tid, token.encode('utf8')
