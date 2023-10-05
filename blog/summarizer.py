from django.utils.html import strip_tags

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

from math import floor


def get_non_stopwords(sentence):
    non_stopwords = []
    for word in word_tokenize(sentence):
        if word.lower() not in stopwords.words('english'):
            non_stopwords.append(word)
    return non_stopwords


def get_words_fdist(sentences):
    non_stopwords = []
    for sentence in sentences:
        sentence_non_stopwords = get_non_stopwords(sentence)
        non_stopwords += sentence_non_stopwords
    fdist = FreqDist(non_stopwords)
    return fdist


def get_content_summary(article_content):
    sentences = sent_tokenize(strip_tags(article_content))
    fdist = get_words_fdist(sentences)

    def sentence_ranker(sentence):
        sentence_non_stopwords = get_non_stopwords(sentence)
        non_stopword_frequencies = [fdist[w] for w in sentence_non_stopwords]
        sentence_rank = sum(non_stopword_frequencies)
        return sentence_rank

    ranked_sentences = sorted(sentences, key=sentence_ranker, reverse=True)
    summary_sentences = min(floor(len(sentences) * 0.2), 4)
    summarized_text = ' '.join(ranked_sentences[:summary_sentences])
    return summarized_text


def has_adequate_length(article_summary):
    sentences = sent_tokenize(article_summary)
    if len(sentences) > 2:
        return True
    return False
