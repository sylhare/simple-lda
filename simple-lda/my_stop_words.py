# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 16:42:04 2016

@author: sylhare
"""

###  STOP WORDS  ###

##  english   ##
# Complete version
CMP_EN = ['a', 'able', 'about', 'above', 'abst', 'accordance', 'according',
          'accordingly', 'across', 'act', 'actually', 'added', 'adj',
          'affected', 'affecting', 'affects', 'after', 'afterwards',
          'again', 'against', 'ah', "ain't", 'all', 'allow', 'allows',
          'almost', 'alone', 'along', 'already', 'also', 'although',
          'always', 'am', 'among', 'amongst', 'an', 'and', 'announce',
          'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone',
          'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'apparently',
          'appear', 'appreciate', 'appropriate', 'approximately', 'are',
          'aren', 'arent', "aren't", 'arise', 'around', 'as', "a's",
          'aside', 'ask', 'asking', 'associated', 'at', 'auth', 'available',
          'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become',
          'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin',
          'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe',
          'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond',
          'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came',
          'can', 'cannot', 'cant', "can't", 'cause', 'causes', 'certain',
          'certainly', 'changes', 'clearly', "c'mon", 'co', 'com', 'come',
          'comes', 'concerning', 'consequently', 'consider', 'considering',
          'contain', 'containing', 'contains', 'corresponding', 'could',
          'couldnt', "couldn't", 'course', "c's", 'currently', 'd', 'date',
          'definitely', 'described', 'despite', 'did', "didn't", 'different',
          'do', 'does', "doesn't", 'doing', 'done', "don't", 'down',
          'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect',
          'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
          'ending', 'enough', 'entirely', 'especially', 'et', 'et-al', 'etc',
          'even', 'ever', 'every', 'everybody', 'everyone', 'everything',
          'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'far',
          'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed',
          'following', 'follows', 'for', 'former', 'formerly', 'forth',
          'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave',
          'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go',
          'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'h', 'had',
          "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't",
          'having', 'he', 'hed', "he'd", "he'll", 'hello', 'help', 'hence',
          'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', "here's",
          'hereupon', 'hers', 'herself', 'hes', "he's", 'hi', 'hid', 'him',
          'himself', 'his', 'hither', 'home', 'hopefully', 'how', 'howbeit',
          'however', "how's", 'hundred', 'i', 'id', "i'd", 'ie', 'if',
          'ignored', "i'll", 'im', "i'm", 'immediate', 'immediately',
          'importance', 'important', 'in', 'inasmuch', 'inc', 'indeed',
          'index', 'indicate', 'indicated', 'indicates', 'information',
          'inner', 'insofar', 'instead', 'into', 'invention', 'inward',
          'is', "isn't", 'it', 'itd', "it'd", "it'll", 'its', "it's",
          'itself', "i've", 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'kg',
          'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately',
          'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let',
          'lets', "let's", 'like', 'liked', 'likely', 'line', 'little', "'ll",
          'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make',
          'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime',
          'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml',
          'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug',
          'must', "mustn't", 'my', 'myself', 'n', 'na', 'name', 'namely',
          'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need',
          'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine',
          'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
          'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'novel', 'now',
          'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off',
          'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one',
          'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise',
          'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
          'overall', 'owing', 'own', 'p', 'page', 'pages', 'part',
          'particular', 'particularly', 'past', 'per', 'perhaps', 'placed',
          'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially',
          'pp', 'predominantly', 'present', 'presumably', 'previously',
          'primarily', 'probably', 'promptly', 'proud', 'provides', 'put',
          'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd',
          're', 'readily', 'really', 'reasonably', 'recent', 'recently',
          'ref', 'refs', 'regarding', 'regardless', 'regards', 'related',
          'relatively', 'research', 'respectively', 'resulted', 'resulting',
          'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say',
          'saying', 'says', 'sec', 'second', 'secondly', 'section', 'see',
          'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self',
          'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven',
          'several', 'shall', "shan't", 'she', 'shed', "she'd", "she'll",
          'shes', "she's", 'should', "shouldn't", 'show', 'showed', 'shown',
          'showns', 'shows', 'significant', 'significantly', 'similar',
          'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody',
          'somehow', 'someone', 'somethan', 'something', 'sometime',
          'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry',
          'specifically', 'specified', 'specify', 'specifying', 'still',
          'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such',
          'sufficiently', 'suggest', 'sup', 'sure', 't', 'take', 'taken',
          'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx',
          'that', "that'll", 'thats', "that's", "that've", 'the', 'their',
          'theirs', 'them', 'themselves', 'then', 'thence', 'there',
          'thereafter', 'thereby', 'thered', 'therefore', 'therein',
          "there'll", 'thereof', 'therere', 'theres', "there's", 'thereto',
          'thereupon', "there've", 'these', 'they', 'theyd', "they'd",
          "they'll", 'theyre', "they're", "they've", 'think', 'third', 'this',
          'thorough', 'thoroughly', 'those', 'thou', 'though', 'thoughh',
          'thousand', 'three', 'throug', 'through', 'throughout', 'thru',
          'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward',
          'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', "t's",
          'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless',
          'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us',
          'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using',
          'usually', 'v', 'value', 'various', "'ve", 'very', 'via', 'viz',
          'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', "wasn't",
          'way', 'we', 'wed', "we'd", 'welcome', 'well', "we'll", 'went',
          'were', "we're", 'werent', "weren't", "we've", 'what', 'whatever',
          "what'll", 'whats', "what's", 'when', 'whence', 'whenever',
          "when's", 'where', 'whereafter', 'whereas', 'whereby', 'wherein',
          'wheres', "where's", 'whereupon', 'wherever', 'whether', 'which',
          'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole',
          "who'll", 'whom', 'whomever', 'whos', "who's", 'whose', 'why',
          "why's", 'widely', 'will', 'willing', 'wish', 'with', 'within',
          'without', 'wonder', 'wont', "won't", 'words', 'world', 'would',
          'wouldnt', "wouldn't", 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd',
          "you'd", "you'll", 'your', 'youre', "you're", 'yours', 'yourself',
          'yourselves', "you've", 'z', 'zero']

# Short Version
SHORTV_EN = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am',
             'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because',
             'been', 'before', 'being', 'below', 'between', 'both', 'but',
             'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't",
             'do', 'does', "doesn't", 'doing', "don't", 'down', 'during',
             'each', 'few', 'for', 'from', 'further', 'had', "hadn't",
             'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd",
             "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself',
             'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll",
             "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's",
             'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my',
             'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only',
             'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over',
             'own', 'same', "shan't", 'she', "she'd", "she'll", "she's",
             'should', "shouldn't", 'so', 'some', 'such', 'than', 'that',
             "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then',
             'there', "there's", 'these', 'they', "they'd", "they'll",
             "they're", "they've", 'this', 'those', 'through', 'to', 'too',
             'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd",
             "we'll", "we're", "we've", 'were', "weren't", 'what', "what's",
             'when', "when's", 'where', "where's", 'which', 'while', 'who',
             "who's", 'whom', 'why', "why's", 'with', "won't", 'would',
             "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your',
             'yours', 'yourself', 'yourselves']


###  FUNCTIONS  ###

def addStopWords(version, words):
    """
    Add Stop Words, words must be string or list of strings.
    It won't be saved at the next launch of the application.

    """

    if not isinstance(words, (list, tuple)):
        words = [words]

    for word in words:
        if isinstance(word, str):
            version.append(word)
        else:
            raise TypeError('Only String or list of strings, can be added',
                            word)

    return 0


def getStopWord(version, *lang):
    """
    The language can be add up later, english as a default

    """
    if version == 'long':
        return CMP_EN
    else:
        return SHORTV_EN


def mStopWords(words, version, *lang):
    """
    Return the list of words without the stopWords
    """
    stop_words = getStopWord(version, *lang)
    words = [word for word in words if word not in stop_words]

    return words
