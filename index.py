from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request # this is request Class from Flask
import requests # This is a third-party Python library that provides a simple and elegant way to make HTTP requests.
import os

app = Flask(__name__)

bot = ChatBot("chatbot", read_only=False,
              logic_adapters=[
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "Sorry, I don't have an answer.",
                      "maximum_similarity_threshold": 0.9
                  }
              ]
              )

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")

# trainer = ListTrainer(bot)
# trainer.train([
#     "hello",
#     "hello!",
#     "How's it going?",
#     "not bad!",
#     "How can I lose weight?",
#     "You've got to work out mate!",
#     "Any suggestion?",
#     "Yes, 1- work out 2- stop eating everything 3- follow a keto diet",
#     "Other suggestions?",
#     "Please visit this link for more info: https://example.com"
# ])

# ROUTING WEB PAGES
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():

    # GET request from Flask
    userText = request.args.get('userMessage')

    # GET request from module requests
    # Get the API key from the environment variable
    api_key = os.getenv("OPENWEATHER_API_KEY")
    rawData = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ userText +"&appid="+api_key)
    result = rawData.json()

    # return str(bot.get_response(userText))
    return result



if __name__=="__main__":
    app.run(debug=True)