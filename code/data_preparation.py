import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
from nltk.tokenize import WordPunctTokenizer
tok = WordPunctTokenizer()

def cleaning(text):
    soup = BeautifulSoup(text, 'lxml')
    soup_text = soup.get_text()
    no_mention = re.sub(r'@[A-Za-z0-9]+','',soup_text)
    no_url = re.sub('https?://[A-Za-z0-9./?/=]+','',no_mention)
    letters_only = re.sub("[^a-zA-Z]", " ", no_url)
    lower_case = letters_only.lower()
    # below steps will remove extra spaces by tokenizing and rejoining them
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()

# handling missing values
def clean_target(data):
    
    data.brand.fillna('missing', inplace = True)
    
    apple = ['iPad', 'iPhone', 'Apple']
    for a in apple:
        data.loc[data['brand'].str.contains(a), 'brand'] = 'Apple'

    android = ['Google', 'Android']
    for a in android:
        data.loc[data['brand'].str.contains(a), 'brand'] = 'Google'

    no_emotion = ["No emotion toward brand or product", "I can't tell"]
    for ne in no_emotion:
        data.loc[data['emotion'] == ne, 'emotion'] = 'none'

    data.loc[data['emotion'].str.contains('Positive'), 'emotion'] = 'Positive'
    data.loc[data['emotion'].str.contains('Negative'), 'emotion'] = 'Negative'
    
    return data

import string
def remove_punctuations(text):
    text = text.replace("/", ' ')
    text = text.replace('quot', '')
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

import re
def removearticles(text):
    text = re.sub('(\s+)(a|an|the)(\s+)', ' ', text)
    text = text.replace('  ', ' ')
    
    return text

def clean_text(data):
    data.tweet_text = data.tweet_text.map(lambda x: x.lower())
    data.tweet_text = data.tweet_text.apply(remove_punctuations)    
    data.tweet_text = data.tweet_text.apply(removearticles)
    
    return data