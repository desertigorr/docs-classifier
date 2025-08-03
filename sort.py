import joblib
from preprocessing import load_clean_docs
import os
import shutil

clf = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

folder_path = "docs_raw"

dir_paths = {"0": "docs_arragned/other",
             "1": "docs_arragned/maths",
             "2": "docs_arragned/physics",
             "3": "docs_arragned/robotics"}

def locate_file(file_path, dir_path):
    file_name = file_path.split("\\")[1]
    shutil.copy(file_path, os.path.join(dir_path, file_name))

def sort_documents(path):
    texts = load_clean_docs(folder_path)
    paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    arr = list(zip(texts, paths))
    for elem in arr:
        text = elem[0]
        path = elem[1]
        X = vectorizer.transform([text])  # Важно подавать список!
        pred = clf.predict(X)
        pred_class = pred[0]
        dir = dir_paths[str(pred_class)]
        locate_file(path, dir)

sort_documents(folder_path)