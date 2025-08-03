from file_scripts import clean_text, extract_from_file
import os

def load_labels(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        labels = [int(line.strip()) for line in file]
    return labels

def load_clean_docs(path):
    paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    raw_texts = [extract_from_file(path) for path in paths]
    clean_texts = [clean_text(text) for text in raw_texts]
    return clean_texts




