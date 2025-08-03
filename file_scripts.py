import os
# Для считывания PDF
import PyPDF2
from pdfminer.high_level import extract_text

# Для считывания docx
from spire.doc import *
from spire.doc.common import *

# Для обработки текста
import re
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import stopwords

# Для лемматизации
import pymorphy3
morph = pymorphy3.MorphAnalyzer()


# Дополняем stopwords словами, которые часто встречаются в отчетах и не несут смысловой нагрузки
stopwords = stopwords.words("russian")
stopwords_augment = ["университет",
                  "итмо",
                  "студент",
                  "лабораторная",
                  "санкт-петербург",
                  "вариант",
                  "факультет",
                  "дисциплина",
                  "задание",
                  "график"]
stopwords.extend(stopwords_augment)

def remove_stopwords(text):
    text = text.split()
    text = [word for word in text if word not in stopwords]
    return " ".join(text)

def lemmatize(text):
    text = text.split(' ')
    text_lemmatized = [list(morph.parse(word)[0])[2] for word in text]
    return " ".join(text_lemmatized)

def clean_text(text):
    text = re.sub(r'[^а-яё\s-]', '', text)
    text = re.sub(r'-\s+', ' ', text)
    text = re.sub(r'\s+-\s+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = remove_stopwords(text)
    text = lemmatize(text)
    return text

def read_pdf(file_path):
    text = extract_text(file_path).lower()
    return text

def read_docx(file_path):
    doc = Document()
    doc.LoadFromFile(file_path)
    text = doc.GetText()
    return text

def extract_from_file(file_path):
    if file_path.endswith(".pdf"):
        try:
            text = read_pdf(file_path)
        except Exception as e:
            print(f"Ошибка: {e}")
    elif file_path.endswith(".docx"):
        try:
            text = read_docx(file_path)
        except Exception as e:
            print(f"Ошибка: {e}")
    if text: return text 
    else: return None












