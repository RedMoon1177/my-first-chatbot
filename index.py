from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

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

trainer = ListTrainer(bot)
trainer.train([
    "hello",
    "hello!",
    "How's it going?",
    "not bad!",
    "How can I lose weight?",
    "You've got to work out mate!",
    "Any suggestion?",
    "Yes, 1- work out 2- stop eating everything 3- follow a keto diet",
    "Other suggestions?",
    "Please visit this link for more info: https://example.com"
])

# ROUTING WEB PAGES
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))



if __name__=="__main__":
    app.run(debug=True)