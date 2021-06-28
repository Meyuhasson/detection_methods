import numpy as np
from feature_extraction import tfidf_extractor
from sklearn.ensemble import RandomForestClassifier

def main():
    random_forest = RandomForestClassifier()
    print("Getting tfidf vectors...")
    benign_tfidf, malicious_tfidf = tfidf_extractor(2,2)
    num_benign_samples = benign_tfidf.shape[0]
    num_malicious_samples = malicious_tfidf.shape[0]
    print("Fitting RFclassifier for benign vectors...")
    random_forest.fit(benign_tfidf,np.zeros((num_benign_samples,1)))
    print("Fitting RFclassifier for malicious vectors...")
    random_forest.fit(malicious_tfidf,np.ones((num_malicious_samples,1)))
    print("HERE")
    
if __name__ == "__main__":
    main()