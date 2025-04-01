'''
In feature set 3 (Table 2), the ten features
 with highest importance values are “has quoted content”,
 “has URL”, “% of uppercase letters”, “frequency of punc
tuation”, “frequency of words of length 15”, “% of
 whitespaces”, “frequency of words of length 14”, “aver
age sentence length in words”, “frequency of words of
 length 12” and “frequency of words of length 11”. In
 Fig. 3, it is observed that real news has a very high aver
age number of quotes compared to fake news.
'''

import pandas as pd
import re
import string



def has_quotes(text):
    return bool(re.search(r'".+"', text))

def has_url(text):
    regex = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    return bool(re.search(regex, text))

def percent_uppercase(text):
    return sum(1 for c in text if c.isupper())/ len(text) * 100 if len(text) > 0 else 0

def frequency_punctuation(text):
    punctuation_set = set(string.punctuation)
    return sum(1 for char in text if char in punctuation_set)

def percent_whitespace(text):
    return text.count(' ')/ len(text) * 100 if len(text) > 0 else 0

def frequency_words_15(text):
    return

