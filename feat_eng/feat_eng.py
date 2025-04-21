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

import re
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

text = "This is a u98u sentence. Here is another! And on'e more?!!!!"

URL_REGEX = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    
def has_quotes(text):
    return int(bool(re.search(r'".+"', text)))

def has_url(text):
    return int(bool(re.search(URL_REGEX, text)))

def percent_uppercase(text):
    return sum(1 for c in text if c.isupper())/ len(text) * 100 if len(text) > 0 else 0

def frequency_punctuation(text):
    punctuation_set = set(string.punctuation)
    return sum(1 for char in text if char in punctuation_set)

def percent_whitespace(text):
    return text.count(' ')/ len(text) * 100 if len(text) > 0 else 0

def frequency_words_length(text, length):
    words = re.findall(r'\b\w{' + str(length) + r'}\b', text) 
    return len(words)

def avg_sentence_length(text):
    sentences = re.split(r'[.?!]', text)
    
    if len(sentences) == 0:
        return 0
    
    total_length = 0
    count = 0
    
    for s in sentences: 
        if len(s) > 0:
            s = s.split(" ")
            total_length += len(s)
            count += 1
    
    return total_length/count if count > 0 else 0

"""
//////////////////////////////////////////////////
                    Iter 2

"""

"""
Built on current feature list
"""

def has_1_to_3_urls(text: str) -> bool:
    count = len(re.findall(URL_REGEX, text))
    return int(1 <= count <= 3)

def has_4_to_6_urls(text: str) -> bool:
    count = len(re.findall(URL_REGEX, text))
    return int(4 <= count <= 6)

def has_more_than_6_urls(text: str) -> bool:
    return int(len(re.findall(URL_REGEX, text)) > 6)


"""
Stylistic features 
"""

#indicates emotion
def num_exclamations(text):
    return text.count('!')

def num_questions(text):
    return text.count('?')

def avg_word_length(text):
    words = re.findall(r'\b\w+\b', text)
    lengths = [len(w) for w in words]
    return sum(lengths) / len(lengths) if lengths else 0

def lexical_diversity(text):
    if not isinstance(text, str):
        return 0
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    unique_words = len(set(words))
    return unique_words / total_words if total_words > 0 else 0

def proportion_stopwords(text):
    if not isinstance(text, str):
        return 0
    words = re.findall(r'\b\w+\b', text.lower())
    if len(words) == 0:
        return 0
    stopwords = [word for word in words if word in ENGLISH_STOP_WORDS]
    return len(stopwords) / len(words)


print(lexical_diversity(text))