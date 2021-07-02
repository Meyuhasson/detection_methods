from feature_extraction import tfidf_extractor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from scipy.sparse import vstack

def main():
    
    print("[+] Extracting TF-IDF vectors from data")
    benign_tfidf, malicious_tfidf = tfidf_extractor(1,1)

    num_benign_samples = benign_tfidf.shape[0]
    num_malicious_samples = malicious_tfidf.shape[0]

    # 0 - benign, 1 - malicious
    benign_classifications = [0 for _ in range(num_benign_samples)]
    malicious_classifications = [1 for _ in range(num_malicious_samples)]

    print("[+] Preparing Train-Test data")
    all_samples = vstack((benign_tfidf,malicious_tfidf))
    all_classes = []
    all_classes.extend(benign_classifications)
    all_classes.extend(malicious_classifications)
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(all_samples, all_classes, random_state=1, stratify=all_classes)

    print("[+] Training Random Forest Classifier")
    random_forest = RandomForestClassifier()
    random_forest.fit(Xtrain,Ytrain)

    print("[+] Evaluating model")
    predict_test = random_forest.predict(Xtest)

    accuracy = accuracy_score(Ytest,predict_test)
    precision = precision_score(Ytest, predict_test)
    recall = recall_score(Ytest, predict_test)

    print(f"\t- Accuracy = {accuracy}") # (tp + tn) / (tp + tn + fp + fn)
    print(f"\t- Precision = {precision}") # tp / (tp + fp)
    print(f"\t- Recall = {recall}") # tp / (tp+fn)
    
if __name__ == "__main__":
    main()