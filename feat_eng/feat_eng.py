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

text = "This is a u98u sentence. Here is another! And on'e more?!!!!"

    
def has_quotes(text):
    return int(bool(re.search(r'".+"', text)))

def has_url(text):
    regex = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    return int(bool(re.search(regex, text)))

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



print(has_quotes(text))