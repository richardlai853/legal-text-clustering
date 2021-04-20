from sentence_transformers import SentenceTransformer
import jieba
import jieba.analyse
import pandas as pd
import re
from sklearn.cluster import KMeans

model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

headers = ["department", "lei", "chapter", "chtitle", "article", "arttitle", "content"]
data = pd.read_csv("lei_cleaned.csv", names=headers)

jieba.set_dictionary('./dict.txt')

stopwords = set([])

with open('stop_words.txt') as f:
    words = f.readlines()

for word in words:
    stopwords.add(word.strip('\n'))

corpus = []

for item in data['content']:
    words = jieba.cut(str(item))
    words = [w for w in words if w not in stopwords]
    words = [w for w in words if len(w) > 1 and not re.match('^[a-z|A-Z|0-9|.]*$', w)]
    item = ' '.join(words)
    corpus.append(item)

# Sentences are encoded by calling model.encode()
corpus_embeddings = model.encode(corpus)

# corpus = []
#
# for s in sentences:
#     k = jieba.cut(s)
#     corpus.append(' '.join(k))

# Perform kmean clustering
num_clusters = 10
clustering_model = KMeans(n_clusters=num_clusters)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

clustered_sentences = [[] for i in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append(corpus[sentence_id])

for i, cluster in enumerate(clustered_sentences):
    print("Cluster ", i+1)
    print(cluster)
    with open('cluster_{}'.format(i), 'w') as f:
        f.writelines(["%s\n" % item for item in cluster])
    print("")
