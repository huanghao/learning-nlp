"""
$ time python learning.py train
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
INFO:root:Model was saved into model.pkl
63.06s user 0.98s system 99% cpu 1:04.62 total

$ python learning.py predict CSDMC2010_SPAM/TESTING.body/TEST_0000*.eml
CSDMC2010_SPAM/TESTING.body/TEST_00000.eml ['1']
CSDMC2010_SPAM/TESTING.body/TEST_00001.eml ['1']
CSDMC2010_SPAM/TESTING.body/TEST_00002.eml ['0']
CSDMC2010_SPAM/TESTING.body/TEST_00003.eml ['0']
CSDMC2010_SPAM/TESTING.body/TEST_00004.eml ['1']
CSDMC2010_SPAM/TESTING.body/TEST_00005.eml ['0']
CSDMC2010_SPAM/TESTING.body/TEST_00006.eml ['1']
CSDMC2010_SPAM/TESTING.body/TEST_00007.eml ['1']
CSDMC2010_SPAM/TESTING.body/TEST_00008.eml ['1']
CSDMC2010_SPAM/TESTING.body/TEST_00009.eml ['0']
"""
import os
import cPickle
import argparse
import logging

from sklearn import svm

from email_features import extract_feature, load_vocab


def train(args):
    if os.path.exists(args.model):
        logging.info('%s already exists, done ..' % args.model)
        return

    with open(args.X) as file:
        X = cPickle.load(file)
    with open(args.y) as file:
        y = cPickle.load(file)

    clf = svm.SVC()
    m = clf.fit(X, y)
    print m
    with open(args.model, 'wb') as file:
        cPickle.dump(m, file)
    logging.info('Model was saved into %s', args.model)


def predict(args):
    with open(args.model) as file:
        m = cPickle.load(file)

    vocab = load_vocab(args.vocabulary)
    for email in args.emails:
        with open(email) as file:
            feature = extract_feature(file.read(), vocab)
        print email, m.predict(feature)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--debug', action='store_true')
    sp = p.add_subparsers()

    train_p = sp.add_parser('train')
    train_p.add_argument('-X', default='X.pkl')
    train_p.add_argument('-y', default='y.pkl')
    train_p.add_argument('-m', '--model', default='model.pkl')
    train_p.set_defaults(func=train)

    predict_p = sp.add_parser('predict')
    predict_p.add_argument('emails', nargs='+')
    predict_p.add_argument('-m', '--model', default='model.pkl')
    predict_p.add_argument('-v', '--vocabulary', default='vocab.txt')
    predict_p.set_defaults(func=predict)
    return p.parse_args()


def main():
    args = parse_args()
    level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=level)

    args.func(args)


if __name__ == '__main__':
    main()
