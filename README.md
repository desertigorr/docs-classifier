# NLP Docs Classifier

### Классификация документов на основе их содержания
Для практики отсортировал мои отчёты к лабам из ИТМО, разбивая на 4 класса ``(maths, physics, robotics, other)``

### Что использовал:
- ``PyPDF2``, ``pdfminer.six``, ``Spire.Doc`` для text extraction из .pdf и .docx файлов
- ``nltk``, ``pymorphy3`` для обработки текста (стоп-слова, лемматизация, очистка от мусора)
- ``sklearn``: ``TfidfVectorizer``, ``RandomForestClassifier``, ``GridSearchCV`` для векторизации текстов и обучения классификатора
- ``joblib`` для сохранения и загрузки векторайзера и модели

### Структура

<pre>
docs-classifier/
├── docs_raw/                                            # Исходные документы
├── docs_arranged/[other/maths/physics/robotics]         # Отсортированные по категориям
├── file_scripts.py                                      # Логика загрузки, чтения и обработки документов
├── preprocessing.py                                     # Итоговые функции для использования (можно убрать)
├── model.py                                             # Обучение TfIdfVectorizer и классификатора
├── sort.py                                              # Скрипт сортировки документов по категориям
├── labels.txt                                           # Метки категорий
└── requirements.txt                                     # Зависимости
 
</pre>
