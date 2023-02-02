import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal
    # despite casing) can be done with
    docs = [line.lower().split() for line in text.split('\n')]
    N = len(docs)
    # 2. go over each unique word and calculate its term frequency, and its document frequency
    tf, df = {}, {}

    vocabulary = list(set(text.lower().split()))

    for word in vocabulary:
        tf[word] = [doc.count(word) / len(doc) for doc in docs]

        df[word] = sum([word in doc for doc in docs]) / N
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and
    # calculate its TF-IDF representation, which will be a vector
    tfidf = []
    for doc_index in range(len(docs)):
        tfidf.append([])
        for i, word in enumerate(vocabulary):
            tfidf[doc_index].append(tf[word][doc_index] * math.log(1 / df[word], 10))

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    find_nearest_pair(tfidf)

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.single)
    for i in range(N):
        for j in range(N):
            sum = 0
            if i == j:
                sum = np.inf
            else:
                for k in range(len(data[i])):
                    sum += abs(data[i][k] - data[j][k])
            dist[i, j] = sum

    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)

