from collections import Counter
words=['humpy','dumpty','together','again','rain','humpy','rain']
counts=Counter(words)
print(counts)

# generating text
import random
texts=random.choices(list(counts.keys()),weights=list(counts.values()),k=20)
print(texts)

# bigram model
bigram=[(words[i], words[i+1]) for i in range(len(
    words)-1)]
print(bigram)