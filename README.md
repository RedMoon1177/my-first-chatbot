# my-first-chatbot

### python using version 3.8.0

### How to use this repo's code:
- git clone the repo
- Run python -m venv .venv -> to create .venv folder inside the project
- Run .\\.venv\Scripts\activate -> activate the virtualenv for this project (→ We’re now using the virtual environment!)

#### activate virtualenv -> install:
- chatterbot
- chatterbot-corpus
- pyyaml #python -m spacy download en_core_web_sm
- spacy
- jupyter
- flask

Note that: if you got the fact that the shortcut 'en' for loading spaCy models is no longer supported as of spaCy v3.0. Instead, you need to use the full name of the model, such as 'en_core_web_sm'.

Step 1: Install the spaCy model: First, make sure the en_core_web_sm model is installed. You can do this by running the following command in your terminal:

   - python -m spacy download en_core_web_sm

Step 2: Update your code: Modify your code to load the full model name instead of the shortcut. Here’s how you can do that:
Open the file C:\WEBDEV\my-first-chatbot\.venv\lib\site-packages\chatterbot\tagging.py and change the following line: 
    - "self.nlp = spacy.load(self.language.ISO_639_1.lower())" to "self.nlp = spacy.load("en_core_web_sm")"

#### To run the script using: 
- Run python index.py

#### Learning from Youtube: 
https://www.youtube.com/playlist?list=PLg4ez-XXTcoMOktk8RU-QEIG_nFuyZdRu
