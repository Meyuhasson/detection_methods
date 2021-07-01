import numpy as np
from feature_extraction import tfidf_extractor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.sparse import vstack
def main():
    random_forest = RandomForestClassifier()
    print("Getting tfidf vectors...")
    benign_tfidf, malicious_tfidf = tfidf_extractor(1,1)
    num_benign_samples = benign_tfidf.shape[0]
    num_malicious_samples = malicious_tfidf.shape[0]
    benign_classifications = np.zeros((num_benign_samples,1))
    malicious_classifications = np.ones((num_malicious_samples,1))

    all_samples = vstack([benign_tfidf,malicious_tfidf]).toarray()
    all_classes = vstack([benign_classifications, malicious_classifications]).toarray()

    Xtrain, Xtest, Ytrain, Ytest = train_test_split(all_samples, all_classes, random_state=1, stratify=all_classes)


    print("Fitting RFclassifier for benign vectors...")
    random_forest.fit(Xtrain,Ytrain)

    predict_test = random_forest.predict(Xtest)

    acc_score = accuracy_score(Ytest,predict_test)
    print(f"Accuracy Score: {acc_score}")
    print("HERE")
    
if __name__ == "__main__":
    main()