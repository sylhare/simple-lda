# -*- coding: utf-8 -*-
"""
LDA training
Latent Dirichlet Allocation with Python

"""

# Source
"""
In the readme file

"""

# Import
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models

# --  Sample Document  -- #

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

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

###  Tokenization  ###

# Converting a document to its atomic elements.
tokenizer = RegexpTokenizer(r'\w+')

"""
The above code will match any word characters until it reaches a
non-word character, like a space.
This is a simple solution, but can cause problems for words like “don’t”
which will be read as two tokens,
“don” and “t.” NLTK provides a number of pre-constructed tokenizers like
nltk.tokenize.simple. For unique use cases,
it’s better to use regex and iterate until your document is accurately
tokenized.

"""

# Example
raw = doc_a.lower()
tokens = tokenizer.tokenize(raw)

print(tokens)
# >> tokens_ouput = ['brocolli', 'is', 'good', 'to', 'eat', 'my', 'brother',
#                   'likes', 'to', 'eat', 'good', 'brocolli', 'but', 'not',
#                   'my', 'mother']


# --  Stop Words  -- #

# create English stop words list
en_stop = get_stop_words('en')

"""
Certain parts of English speech, like conjunctions (“for”, “or”)
or the word “the” are meaningless to a topic model.
These terms are called stop words and need to be removed from our token list.

The definition of a stop word is flexible and the kind of documents
may alter that definition.
For example, if we’re topic modeling a collection of music reviews,
then terms like “The Who” will have trouble being surfaced because “the”
is a common stop word and is usually removed.
You can always construct your own stop word list or seek out another package
to fit your use case.

"""

stopped_tokens = [i for i in tokens if not i in en_stop]

# --  Stemming  -- #

# import the Porter Stemmer module from NLTK
# from nltk.stem.porter import PorterStemmer

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

"""
Stemming words is another common NLP technique to reduce topically similar
words to their root. For example, “stemming,” “stemmer,” “stemmed,”
all have similar meanings; stemming reduces those terms to “stem.”
This is important for topic modeling, which would otherwise view those terms
as separate entities and reduce their importance in the model.

Like stopping, stemming is flexible and some methods are more aggressive.
The Porter stemming algorithm is the most widely used method
"""

# Example, stem token
stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

print(stemmed_tokens)
# >> texts = ['brocolli', 'good', 'eat', 'brother', 'like',
#            'eat', 'good', 'brocolli', 'mother']

"""Contructing a document-term matrix"""

"""
The result of our cleaning stage is texts, a tokenized, stopped and stemmed
list of words from a single document. Let’s fast forward and imagine that we
looped through all our documents and appended each one to texts. So now texts
is a list of lists, one list for each of our original documents.

"""

# Construct a document-term matrix with a package called gensim
# from gensim import corpora, models
texts.append(stemmed_tokens)
dictionary = corpora.Dictionary(texts)

"""
The Dictionary() function traverses texts, assigning a unique integer id to
each unique token while also collecting word counts and relevant statistics.
To see each token’s unique integer id, try print(dictionary.token2id)

"""

# dictionary must be converted into a bag-of-words
corpus = [dictionary.doc2bow(text) for text in texts]

# --  Generating the LDA model -- #
# Source : Jordan Barber


tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=2,
                                    id2word=dictionary, passes=20)
