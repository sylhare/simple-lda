# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:28:15 2017

@author: sylhare
"""

###  My LDA Training  ###

import my_stop_words as msw
import my_tokenize as mt
import my_stemming_algo as msa

###  Sample Document  ###

# Text
doc_a = """Brocolli is good to eat. My brother likes to eat good brocolli,
        but not my mother."""
doc_b = """My mother spends a lot of time driving my brother around
        to baseball practice."""
doc_c = """Some health experts suggest that driving may cause increased
        tension and blood pressure."""
doc_d = """I often feel pressure to perform well at school, but my mother
        never seems to drive my brother to do better."""
doc_e = """Health professionals say that brocolli is good for your health."""

raw = doc_a.lower()

###  Tokenization  ###
tokens = mt.mTokenize(raw)

###  Stop Words  ###
# remove stop words from tokens
stopped_tokens = msw.mStopWords(tokens, 'long')

print(stopped_tokens)
# >> ['brocolli', 'good', 'eat', 'brother', 'likes', 'eat', 'good',
#     'brocolli', 'mother']

###  Stemming  ###
# It is based on the porter stemmer
