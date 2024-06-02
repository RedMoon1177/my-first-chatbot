# my-first-chatbot

### python using version 3.8.0

### How to use this repo's code:
- git clone the repo
- Run python -m venv .venv -> to create .venv folder inside the project
- Run .\\.venv\Scripts\activate -> activate the virtualenv for this project (→ We’re now using the virtual environment!)

#### After activating virtualenv -> then install:
1. chatterbot (https://chatterbot.readthedocs.io/en/stable/)
2. chatterbot-corpus 
3. run "python -m chatterbot_corpus download english" (downloading the English Corpus)
(this is a built-in corpus of conversational data for training chatbots in different languages, including English)
   - Another option for training data: use English language model for spaCy, a popular natural language processing (NLP) library in Python. 
   - install spacy -> run "python -m spacy download en"
4. pyyaml (run pip install PyYAML==3.13)
5. jupyter (a popular open-source web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text)
6. flask (a lightweight and extensible web framework for Python)
7. pint (a Python package to define, operate and manipulate physical quantities)

(for example: Run "pip install chatterbot")

Note that: if you got the fact that the shortcut 'en' for loading spaCy models is no longer supported as of spaCy v3.0. Instead, you need to use the full name of the model, such as 'en_core_web_sm'.

**Step 1**: Install the spaCy model: First, make sure the en_core_web_sm model is installed. You can do this by running the following command in your terminal:

   - python -m spacy download en_core_web_sm

**Step 2**: Update your code: Modify your code to load the full model name instead of the shortcut. Here’s how you can do that:
Open the file C:\WEBDEV\my-first-chatbot\.venv\lib\site-packages\chatterbot\tagging.py and change the following line: 
    - "self.nlp = spacy.load(self.language.ISO_639_1.lower())" to "self.nlp = spacy.load("en_core_web_sm")"

#### To run the script using: 
- Run python index.py

#### Set environment variables:
- On Windows:
Open Command Prompt or PowerShell and run: setx OPENWEATHER_API_KEY "your_api_key_here"
- On macOS/Linux:
Open your terminal and run: export OPENWEATHER_API_KEY="your_api_key_here"

#### Learning from Youtube: 
https://www.youtube.com/playlist?list=PLg4ez-XXTcoMOktk8RU-QEIG_nFuyZdRu
