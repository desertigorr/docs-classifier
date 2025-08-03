from preprocessing import load_clean_docs, load_labels
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
import joblib

folder_path = "docs_raw"
labels_path = "labels.txt"

labels_disamb = {"0": "other",
                 "1": "maths",
                 "2": "physics",
                 "3": "robotics"}

labels = load_labels(labels_path)
print(f"labels: {labels.count(0)} other, {labels.count(1)} maths, {labels.count(2)} physics, {labels.count(3)} robotics")
texts = load_clean_docs(folder_path)

print('start vectorizer')
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_df=0.9, min_df=2)
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=78)

clf = RandomForestClassifier(random_state=78)

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20, None],
    'max_features': ['sqrt', 'log2']
}

grid_search = GridSearchCV(
    estimator=clf,
    param_grid=param_grid,
    cv=5,  # 
    scoring='f1_macro', 
    n_jobs=4,  
    verbose=2  
)

grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)

best_clf = grid_search.best_estimator_
y_pred = best_clf.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(best_clf, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')


