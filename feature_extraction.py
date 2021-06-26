import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import js_extraction

def tfidf_extractor(ngramx,ngramy):
    list_of_vectors_benign = []
    list_of_vectors_malicious = []
    for tokens in js_extraction.get_all_js_token(True):
        if not tokens:
            continue
        flat_list = []
        for token in tokens:
            flat_list.append(token.type)
            flat_list.append(token.value)
        vectorizer = TfidfVectorizer(ngram_range = (ngramx, ngramy))
        X = vectorizer.fit_transform(flat_list)
        list_of_vectors_benign.append(X)
    for tokens in js_extraction.get_all_js_token(False):
        if not tokens:
            continue
        flat_list = []
        for token in tokens:
            flat_list.append(token.type)
            flat_list.append(token.value)
        vectorizer = TfidfVectorizer(ngram_range = (ngramx, ngramy))
        X = vectorizer.fit_transform(flat_list)
        list_of_vectors_malicious.append(X)
    return list_of_vectors_benign, list_of_vectors_malicious

list_of_vectors_benign, list_of_vectors_malicious = tfidf_extractor(1,1)
