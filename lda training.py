"""LDA training"""

#Source
"""
http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/
https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html
https://radimrehurek.com/gensim/models/ldamodel.html
http://snowball.tartarus.org/algorithms/english/stemmer.html
"""

#Import
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import my_stop_words as msw

import gensim


"""Sample Document"""

#Text
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]



"""Tokenization"""

#Converting a document to its atomic elements.
tokenizer = RegexpTokenizer(r'\w+')

"""
The above code will match any word characters until it reaches a non-word character, like a space. 
This is a simple solution, but can cause problems for words like “don’t” which will be read as two tokens, 
“don” and “t.” NLTK provides a number of pre-constructed tokenizers like nltk.tokenize.simple. For unique use cases, 
it’s better to use regex and iterate until your document is accurately tokenized.
"""

#Example
raw = doc_a.lower()
tokens = tokenizer.tokenize(raw)

print(tokens)
tokens_ouput = ['brocolli', 'is', 'good', 'to', 'eat', 'my', 'brother', 'likes', 'to', 'eat', 'good', 'brocolli', 'but', 'not', 'my', 'mother']

#Method
def mTokenize(text):
    punctuation = [',','.','?','!',':',';',] #Words with "'" will be removed in the stop words part
    text.lower()
    
    #Remove punctuation
    for x in punctuation:
        text = text.replace(x,"")
   
    #Decompose the text into words
    output = text.split(" ")
    
    return output



"""Stop Words"""

# create English stop words list
en_stop = get_stop_words('en')

"""
Certain parts of English speech, like conjunctions (“for”, “or”) or the word “the” are meaningless to a topic model.
These terms are called stop words and need to be removed from our token list.

The definition of a stop word is flexible and the kind of documents may alter that definition. 
For example, if we’re topic modeling a collection of music reviews,
then terms like “The Who” will have trouble being surfaced because “the” is a common stop word and is usually removed.
You can always construct your own stop word list or seek out another package to fit your use case.
"""

# remove stop words from tokens
stopped_tokens = [i for i in tokens if not i in en_stop]

print(stopped_tokens)
['brocolli', 'good', 'eat', 'brother', 'likes', 'eat', 'good', 'brocolli', 'mother']

# Method
def mStopWords(liste):
    stopWords = msw.setStopWords('long')
    liste = [e for e in liste if e not in stopWords]
    
    return liste


"""Stemming"""

# import the Porter Stemmer module from NLTK
from nltk.stem.porter import PorterStemmer

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

"""Stemming words is another common NLP technique to reduce topically similar words to their root. For example, “stemming,” “stemmer,” “stemmed,” all have similar meanings; stemming reduces those terms to “stem.” This is important for topic modeling, which would otherwise view those terms as separate entities and reduce their importance in the model.

Like stopping, stemming is flexible and some methods are more aggressive. The Porter stemming algorithm is the most widely used method"""

#Example, stem token
texts = [p_stemmer.stem(i) for i in stopped_tokens]

print(stemmed_tokens)
['brocolli', 'good', 'eat', 'brother', 'like', 'eat', 'good', 'brocolli', 'mother']

#Method
vowels = "aeiouy" #Takes less memory space?
doubles = ("bb", "dd", "ff", "gg", "mm", "nn", "pp", "rr", "tt")
li_ending = "cdeghkmnrt"

"""
R1 is the region after the first non-vowel following a vowel, or is the null region at the end of the word if there is no such non-vowel.
R2 is the region after the first non-vowel following a vowel in R1, or is the null region at the end of the word if there is no such non-vowel. 

Below, R1 and R2 are shown for a number of English words,

    b   e   a   u   t   i   f   u   l
                      |<------------->|    R1
                              |<----->|    R2
"""

word="Testerization"
#Return the r1 of word, or the r2 of a r1
#r1 = region(word) and r2 = region(word)
def region(word):
    for c in range(1,len(word)):
        if word[c] not in vowels and word[c-1] in vowels:
            return word[c+1:]
    return ""

#To djust the size of the root (r1 and r2) after removing a suffix
#Not used because I've over simplified the code
def adjust(r, suffix):
    if len(r) >= len(suffix):
        r = r[:-len(suffix)]
    else:
        r = ""
    return r

#For some step, replace suffix that are in r1 by there counterpart
#suffix is a list of tuples, suffix=[(suffix to replace, counterpart)]
def replaceSuffix(word,suffix):      
    for s in suffix: 
        if word.endswith(s[0]) and region(word).endswith(s[0]):  
            return word[:-len(s[0])] + s[1] 
    return word   

#Define if the last syllable is a short syllable or not
#A short word is a word that ends with a short syllable
def isLastShort(word):
    if len(word) >= 3 and (word[-1] not in vowels and 
                           word[-1] not in 'wx'and
                           word[-2] in vowels and
                           word[-3] not in vowels):
        return True
    return False

"""STEP 0 """
#The ' and 's and 's' are either removed by the tokenization or because it's a stop word

"""STEP 1A"""
#Replace 'sses'
if word.endswith('sses'): 
    word=word[:-2]

#Replace 'ied' and 'ies' by 'i' if preceded by more than one letter otherwise by 'ie'
if word.endswith('ied') or word.endswith('ies'):    
    if len(word) >= 4:
        word = word[:-1]
    else:
        word = word[:-2]

#Keep the 's' only for 1 vowel words that gas their vowel just before the 's'
#So gas and this retain the s, gaps and kiwis lose it
#if ends with 'us' or 'ss' do nothing
if word.endswith('s') and not (word.endswith('ss') or word.endswith('us')):
    for letter in word[:-2]:
        if letter in vowels:
            word = word[:-1]
            break

            
"""STEP 1B"""
#eed, eedly, ed, edly, ing, ingly
suffix1 = [('eed', 'ee'), ('eedly', 'ee')]
word = replaceSuffix(word,suffix1)

for s in ('ed', 'edly', 'ing', 'ingly'):
    if word.endswith(s):
        for letter in word:
            if letter in vowels:
                word = word[:-len(s)]
                break
        break 

if word.endswith(('at', 'bl', 'iz')):
    word = word+'e'
    
if word.endswith(doubles):
    word = word[:-1]
    if region(word) == "" and isLastShort(word):
        word = word + 'e'
    
print (word)


"""STEP 1C"""
#Not necessary, mostly replacing "y" by "i"

 
"""STEP 2 """
#Not so sure with ('ivity','ive') - Active and Activity, ('ogy','og') - biology and biolog
word = "affirmation"
#word = "inaction"
suffix2 = [('tional','tion'), ('ency','ence'), ('ancy','ance'), ('ably','able'),
        ('ently','ent'), ('izer','ize'), ('ization','ize'), ('ational','ate'),
        ('ation','ate'), ('ator','ate'), ('alism','al'), ('ality','al'), ('ally','al'),
        ('fulness','ful'), ('ousli','ous'), ('ousness','ous'), ('iveness','ive'),
        ('bility','ble'), ('bly','ble'), ('fully','ful'), ('lessly','less')]

word = replaceSuffix(word,suffix2)
print (word)

if word.endswith('ly') and word[-3] in li_ending:
    word = word [:-2]

    
"""STEP 3 """
#Mostly do same as step 2 but to remove last suffix (like in rationalization)
suffix3 = [('tional','tion'), ('ational','ate'), ('alize','al'), ('icate','ic'),
         ('icity','ic'), ('ical','ic'), ('ful',''), ('ness','')]  
         
word = replaceSuffix(word,suffix3)

#ative to delete in some time is optional


"""STEP 4 """
#Mettre à jour R1,R2 dans les autres étapes
suffix4 = ['al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement',
         'ment', 'ent', 'ism', 'ate', 'iti', 'ous', 'ive', 'ize']
         
r2 = region(region(word)) 

for s in suffix4:
    if r2.endswith(s): 
        word=word.replace(s,'')
        break
    
if r2.endswith('ion') and (word[:-3].endswith('s') or word[:-3].endswith('t')):
    word=word[:-3]
    

"""STEP 5 """
#A short syllable in a word is a vowel followed by a non-vowel other than w, x
# "---oos" is not a short syllabe, "---os" is a short syllabe
r1 = region(word)
r2 = region(r1) 

if r2.endswith('e'):
    word = word[:-1]
elif r1.endswith('e'):
    if not isLastShort(word[:-1]):
        word = word[:-1]
    
print (word)

"""Contructing a document-term matrix"""

"""The result of our cleaning stage is texts, a tokenized, stopped and stemmed list of words from a single document. Let’s fast forward and imagine that we looped through all our documents and appended each one to texts. So now texts is a list of lists, one list for each of our original documents."""

#Construct a document-term matrix with a package called gensim
from gensim import corpora, models
dictionary = corpora.Dictionary(texts)

"""The Dictionary() function traverses texts, assigning a unique integer id to each unique token while also collecting word counts and relevant statistics. To see each token’s unique integer id, try print(dictionary.token2id)"""

#dictionary must be converted into a bag-of-words
corpus = [dictionary.doc2bow(text) for text in texts]
