import cPickle
import os
import sys

import nltk
from nltk.corpus.reader import plaintext
from nltk.corpus.reader import util

CORPUS_DIR = 'twitter_normalized'

def get_corpus(corpus_root):
  return plaintext.PlaintextCorpusReader(
    corpus_root, '.*', para_block_reader=util.read_line_block)

def get_nn_terminated_trigrams(sent):
  tagged = nltk.pos_tag(sent)
  for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(tagged):
    if t3.startswith('NN'):
      yield ((w1,t1), (w2,t2), (w3,t3))

def concordance_across(corpus):
  for fileid in ('audiodude', 'itsabbyyyyy', 'BarackObama', 'konklone'):
    text = nltk.Text(corpus.words(fileid))
    print(fileid)
    print('%s - %s' % (text.count(sys.argv[1]), sys.argv[1]))
    text.concordance(sys.argv[1])


if __name__ == '__main__':
  corpus_root = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             CORPUS_DIR)
  corpus = get_corpus(corpus_root)

  concordance_across(corpus)

  # fileids = ('audiodude',)  # ('audiodude', 'itsabbyyyyy', 'BarackObama'):
  # for fileid in fileids:
  #   for sent in corpus.sents('audiodude'):
  #     for tri in get_nn_terminated_trigrams(sent):
  #       print(' '.join(t[0] for t in tri))
