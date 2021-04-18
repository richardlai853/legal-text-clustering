# -*- coding: utf-8 -*-
from gensim.corpora import WikiCorpus
import os


class Config:
    data_path = ''
    zhwiki_bz2 = 'zhwiki-latest-pages-articles.xml.bz2'
    zhwiki_raw = 'zhwiki_raw.txt'


def data_process(_config):
    i = 0
    output = open(os.path.join(_config.data_path, _config.zhwiki_raw), 'w')
    wiki = WikiCorpus(os.path.join(_config.data_path, _config.zhwiki_bz2), lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(' '.join(text) + '\n')
        i += 1
        if i % 10000 == 0:
            print('Saved ' + str(i) + ' articles')
    output.close()
    print('Finished Saved ' + str(i) + ' articles')

config = Config()
data_process(config)