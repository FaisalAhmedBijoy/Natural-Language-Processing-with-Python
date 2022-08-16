import re
import os
from pprint import pprint
from collections import Counter

def corpus_generation(corpus_text_path):
    with open(corpus_text_path, 'r') as f:
        corpus_text = f.read()
    return corpus_text


def cleanup_corpus_and_tokenization(corpus):
    # print(corpus)
    # remove punctuation
    text = re.sub(r"[^a-zA-Z0-9.?]", " ", corpus)
    # print(text)
    words=text.split()
    return words

def unigram_probabilities(words):
    p_unigrams=Counter(words)
    # print(p_unigrams)
    return p_unigrams
    # return list(p_unigrams.values())

def bigram_probabilities(words):
    # bigram_dict = {words[i]: words[i + 1] for i in range(len(words) - 1)}
    # p_bigrams = Counter(bigram_dict)
    # pprint(p_bigrams)
    # return p_bigrams
    # calculate bigram probability
    p_bigrams={}
    num_bigrams =0
    for x in range(len(words) - 1):
        if words[x] in p_bigrams:
            if words[x + 1] in p_bigrams[words[x]]:
                p_bigrams[words[x]][words[x + 1]] += 1
            else:
                p_bigrams[words[x]][words[x + 1]] = 1
                num_bigrams += 1
        else:
            p_bigrams[words[x]] = {}
            p_bigrams[words[x]][words[x + 1]] = 1
            num_bigrams += 1
    pprint(p_bigrams)
    return p_bigrams

if __name__ == '__main__':
    corpus_text_path='carrol_alice.txt'
    corpus=corpus_generation(corpus_text_path)
    words=cleanup_corpus_and_tokenization(corpus)
    p_unigrams=unigram_probabilities(words)
    p_bigrams=bigram_probabilities(words)



