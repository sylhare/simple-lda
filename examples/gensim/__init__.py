# Download stopwords and wordnet if not there.
import string

try:
    from nltk.corpus import stopwords
    from nltk.stem.wordnet import WordNetLemmatizer
except LookupError:
    import nltk

    nltk.download('stopwords')
    nltk.download('wordnet')

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)


def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(WordNetLemmatizer().lemmatize(word) for word in punc_free.split())
    return normalized
