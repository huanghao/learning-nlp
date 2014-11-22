"""
$ python email_features.py CSDMC2010_SPAM/TRAINING.body vocab.txt CSDMC2010_SPAM/SPAMTrain.label
..
INFO:root:X: (4327, 1566) -> X.pkl
INFO:root:y: (4327,) -> y.pkl

$ ls -lh *.pkl
-rw-r--r--  1 huanghao  staff   206M Nov 22 20:35 X.pkl
-rw-r--r--  1 huanghao  staff   4.4K Nov 22 20:35 y.pkl
"""
import sys
import logging
import cPickle

import numpy as np

from make_vocab import walk_emails


def load_vocab(fname):
    vocab = {}
    with open(fname) as file:
        for line in file:
            tid, token = line.rstrip().split(None, 1)
            vocab[token] = int(tid)
    return vocab


def extract_feature(text, vocab):
    feature = np.zeros(len(vocab))
    for word in text.split():
        tid = vocab.get(word, None)
        if tid is not None:
            feature[tid-1] = 1
    return feature


def build_data(top, vocab_fname):
    vocab = load_vocab(vocab_fname)
    features = []
    for fname, content in walk_emails(top):
        logging.debug('processing %s ..', fname)
        f = extract_feature(content, vocab)
        features.append(f)
    return np.vstack(features)


def build_target(label_fname):
    target = []
    with open(label_fname) as file:
        for line in file:
            t, _ = line.split(None, 1)
            target.append(t)
    return np.array(target)


def build(top, vocab_fname, label_fname):
    X = build_data(top, vocab_fname)
    y = build_target(label_fname)

    xname = 'X.pkl'
    with open(xname, 'wb') as file:
        cPickle.dump(X, file)
    logging.info('X: %s -> %s', X.shape, xname)

    yname = 'y.pkl'
    with open(yname, 'wb') as file:
        cPickle.dump(y, file)
    logging.info('y: %s -> %s', y.shape, yname)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    build(*sys.argv[1:])
