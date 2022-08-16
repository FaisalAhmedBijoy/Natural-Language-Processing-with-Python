import re
import os
import random
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
    # pprint(p_bigrams)
    return p_bigrams

def generate_sequence(p_unigrams,p_bigrams,num_words=100,seed_word=None):
    if seed_word is None:
        seed_word = random.choices(list(p_unigrams.keys()), weights=list(p_unigrams.values()))[0]
    seq = [seed_word]
    print(seq)
    for i in range(num_words):
        seq.append(random.choices(list(p_bigrams[seq[-1]].keys()), weights=list(p_bigrams[seq[-1]].values()))[0])
    return seq

if __name__ == '__main__':
    corpus_text_path='carrol_alice.txt'
    corpus=corpus_generation(corpus_text_path)
    words=cleanup_corpus_and_tokenization(corpus)
    p_unigrams=unigram_probabilities(words)
    p_bigrams=bigram_probabilities(words)
    sequence=generate_sequence(p_unigrams,p_bigrams)
    print(sequence)




