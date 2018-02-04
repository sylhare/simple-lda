# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 06:22:40 2016

Based on the Porter Algorithm
http://snowball.tartarus.org/algorithms/english/stemmer.html
http://tartarus.org/~martin/PorterStemmer/def.txt
http://www.nltk.org/_modules/nltk/stem/snowball.html
R1 and R2: http://snowball.tartarus.org/texts/r1r2.html

@author: sylhare
"""

# vowels = ['a','e','i','o','u','y']
vowels = "aeiouy"  # Takes less memory space?
doubles = ("bb", "dd", "ff", "gg", "mm", "nn", "pp", "rr", "tt")
li_ending = "cdeghkmnrt"

"""
R1 is the region after the first non-vowel following a vowel, or is the null
region at the end of the word if there is no such non-vowel.
R2 is the region after the first non-vowel following a vowel in R1,
or is the null region at the end of the word if there is no such non-vowel.

Below, R1 and R2 are shown for a number of English words,

    b   e   a   u   t   i   f   u   l
                      |<------------->|    R1
                              |<----->|    R2
"""
word = "Testerization"


def region(word):
    """
    Return the r1 of word, or the r2 of a r1
    r1 = region(word) and r2 = region(word)

    """
    for c in range(1, len(word)):
        if word[c] not in vowels and word[c - 1] in vowels:
            return word[c + 1:]
    return ""


def adjust(r, suffix):
    """
    To djust the size of the root (r1 and r2) after removing a suffix
    Not used because I've over simplified the code

    """
    if len(r) >= len(suffix):
        r = r[:-len(suffix)]
    else:
        r = ""
    return r


def replaceSuffix(word, suffix):
    """
    For some step, replace suffix that are in r1 by there counterpart
    suffix is a list of tuples, suffix=[(suffix to replace, counterpart)]

    """
    for s in suffix:
        if word.endswith(s[0]) and region(word).endswith(s[0]):
            return word[:-len(s[0])] + s[1]
    return word


def isLastShort(word):
    """
    Define if the last syllable is a short syllable or not
    A short word is a word that ends with a short syllable

    """
    if len(word) >= 3 and (word[-1] not in vowels and
                           word[-1] not in 'wx' and
                           word[-2] in vowels and
                           word[-3] not in vowels):
        return True
    return False


###  STEP 0  ###
# The ' and 's and 's' are either removed by the tokenization
# or because it's a stop word

###  STEP 1A  ###
# Replace 'sses'
if word.endswith('sses'): word = word[:-2]

# Replace 'ied' and 'ies' by 'i' if preceded by
# more than one letter otherwise by 'ie'
if word.endswith('ied') or word.endswith('ies'):
    if len(word) >= 4:
        word = word[:-1]
    else:
        word = word[:-2]

# Keep the 's' only for 1 vowel words that gas their vowel just before the 's'
# So gas and this retain the s, gaps and kiwis lose it
# if ends with 'us' or 'ss' do nothing
if word.endswith('s') and not (word.endswith('ss') or word.endswith('us')):
    for letter in word[:-2]:
        if letter in vowels:
            word = word[:-1]
            break

###  STEP 1B  ###
# eed, eedly, ed, edly, ing, ingly
suffix1 = [('eed', 'ee'), ('eedly', 'ee')]
word = replaceSuffix(word, suffix1)

for s in ('ed', 'edly', 'ing', 'ingly'):
    if word.endswith(s):
        for letter in word:
            if letter in vowels:
                word = word[:-len(s)]
                break
        break

if word.endswith(('at', 'bl', 'iz')):
    word = word + 'e'

if word.endswith(doubles):
    word = word[:-1]
    if region(word) == "" and isLastShort(word):
        word = word + 'e'

print(word)

###  STEP 1C  ###

# Not very necessary, mostly replacing "y" by "i"


###  STEP 2  ###

# Not so sure that step 1 is optionnal with
# ('ivity','ive') - Active and Activity, ('ogy','og') - biology and biolog

word = "affirmation"
# word = "inaction"
suffix2 = [('tional', 'tion'), ('ency', 'ence'), ('ancy', 'ance'), ('ably', 'able'),
           ('ently', 'ent'), ('izer', 'ize'), ('ization', 'ize'), ('ational', 'ate'),
           ('ation', 'ate'), ('ator', 'ate'), ('alism', 'al'), ('ality', 'al'),
           ('ally', 'al'), ('fulness', 'ful'), ('ousli', 'ous'), ('ousness', 'ous'),
           ('iveness', 'ive'), ('bility', 'ble'), ('bly', 'ble'), ('fully', 'ful'),
           ('lessly', 'less')]

word = replaceSuffix(word, suffix2)
print(word)

if word.endswith('ly') and word[-3] in li_ending:
    word = word[:-2]

###  STEP 3  ###

# Mostly do same as step 2 but to remove last suffix (like in rationalization)
suffix3 = [('tional', 'tion'), ('ational', 'ate'), ('alize', 'al'), ('icate', 'ic'),
           ('icity', 'ic'), ('ical', 'ic'), ('ful', ''), ('ness', '')]

word = replaceSuffix(word, suffix3)

# ative to delete in some time is optional


###  STEP 4  ###
# Mettre à jour R1,R2 dans les autres étapes
suffix4 = ['al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement',
           'ment', 'ent', 'ism', 'ate', 'iti', 'ous', 'ive', 'ize']

r2 = region(region(word))
for s in suffix4:
    if r2.endswith(s):
        word = word.replace(s, '')
        break

if r2.endswith('ion') and (word[:-3].endswith('s') or word[:-3].endswith('t')):
    word = word[:-3]

###  STEP 5  ###
# A short syllable in a word is a vowel followed by a non-vowel other than w, x
# "---oos" is not a short syllabe, "---os" is a short syllabe
r1 = region(word)
r2 = region(r1)

if r2.endswith('e'):
    word = word[:-1]
elif r1.endswith('e') and not isLastShort(word[:-1]):
    word = word[:-1]

print(word)
