# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:18:53 2016

@author: sylhare
"""


### FONCTION ###

def mTokenize(text):
    """
    Returns a tokenize version of the input text

    """
    # Words with "'" will be removed in the stop words part
    # punctuation = [',','.','?','!',':',';','(',')', "'","'s","'s'"]
    punctuation = [',', '.', '?', '!', ':', ';', '(', ')']
    text.lower()

    # Remove punctuation
    for x in punctuation:
        text = text.replace(x, "")

    # Decompose the text into words
    output = text.split(" ")

    return output
