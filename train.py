import logging
import multiprocessing
from optparse import OptionParser
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec, Doc2Vec
from gensim.models.word2vec import LineSentence
import gensim
import smart_open


def read_corpus(fname, tokens_only=False):
    with smart_open.open(fname) as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

infile = 'zhwiki_t_seg.txt'
outmodel = 'zhwiki.word2vec.model'
outvector = 'zhwiki.word2vec.vectors'

train_corpus = list(read_corpus(infile))

model = Doc2Vec(train_corpus, vector_size=50, min_count=2, epochs=40)
model.save(outmodel)
