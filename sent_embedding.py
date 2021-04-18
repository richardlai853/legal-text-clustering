from sentence_transformers import SentenceTransformer
import jieba

model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

# Our sentences we like to encode
sentences = ['人生自古誰無死',
             '每個人一天內都需要做兩件他討厭的事',
             '你站在歷史的正確面']

# Sentences are encoded by calling model.encode()
sentence_embeddings = model.encode(sentences)

corpus = []

for s in sentences:
    k = jieba.cut(s)
    corpus.append(' '.join(k))

# Print the embeddings
for sentence, embedding in zip(corpus, sentence_embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
