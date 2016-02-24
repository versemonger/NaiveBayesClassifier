"""
This script calculates how many top 100 key words
each category has and outputs the result in the
file categorical_key_words.
It needs an input file named
TopWordsCountsInDifferentCategories,
which can be gained by executing
NaiveBayesianClassifier.py -t
The result is output in file
categorical_key_words
"""

import numpy as np

counts = np.loadtxt("TopWordsCountsInDifferentCategories")
shape = np.shape(counts)
rows = shape[0]
columns = shape[1]
for i in range(rows):
    for j in range(columns):
        if counts[i][j] > 0:
            counts[i][j] = 1
category_key_words = np.sum(counts, axis=0)
np.savetxt("categorical_key_words", category_key_words, fmt="%d")
