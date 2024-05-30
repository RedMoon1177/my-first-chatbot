from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

# list to train is a list of pairs of [ user's input - chatbot's response " ]
list_to_train = [
                    "Hi!",
                    "Hi there!",
                    "What's your name?",
                    "I'm a chatbot.",
                    "How old are you?",
                    "I'm ageless!",
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)

while True:
    user_response = input("User: ")
    print("Chatbot: ", bot.get_response(user_response))