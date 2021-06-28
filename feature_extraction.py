from sklearn.feature_extraction.text import TfidfVectorizer
import js_extraction

def tfidf_extractor(ngramx,ngramy):
    flat_benign = []
    flat_malicious = []
    list_of_vectors_benign = []
    list_of_vectors_malicious = []

    print("Extracting benign...")
    for tokens in js_extraction.get_all_js_token(True):
        if not tokens:
            continue
        flat_list = []
        for token in tokens:
            flat_list.append(token.type)
            flat_list.append(token.value)
        flat_benign.append(" ".join(flat_list))

    print("Extracting malicious...")
    for tokens in js_extraction.get_all_js_token(False):
        if not tokens:
            continue
        flat_list = []
        for token in tokens:
            flat_list.append(token.type)
            flat_list.append(token.value)
        flat_malicious.append(" ".join(flat_list))
    
    vectorizer = TfidfVectorizer(ngram_range=(ngramx,ngramy))
    vectorizer.fit(flat_benign)

    #Do we need to train on malicious?
    #vectorizer.fit(flat_malicious)
    
    list_of_vectors_benign = vectorizer.transform(flat_benign)
    list_of_vectors_malicious = vectorizer.transform(flat_malicious)

    return list_of_vectors_benign, list_of_vectors_malicious

#list_of_vectors_benign, list_of_vectors_malicious = tfidf_extractor(1,1)
