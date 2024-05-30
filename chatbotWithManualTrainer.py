from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# bot = ChatBot("chatbot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

bot = ChatBot("chatbot", read_only=False, 
                logic_adapters=[
                        {
                            "import_path":"chatterbot.logic.BestMatch",
                            "default_response":"Sorry I don't have an answer", # this is the last chatbot's choice
                            "maximum_similarity_threshold": 0.9
                        }
                    ]
             )


# list to train is a list of pairs of [ user's input - chatbot's response " ]
list_to_train = [
                    "Hi!",
                    "Hi there!",
                    "What's your name?",
                    "I'm a chatbot.",
                    "How old are you?",
                    "I'm ageless!",
                    "Why are you so mad?",
                    "I'm not!",
                    "Do you have iPhone?",
                    "I have everything!",
                    "What's your favorite food?",
                    "I don't eat!",
                    "What's your job?",
                    "I'm here to answer your questions!",
                    "I don't know what you're talking about!"
]

list_to_train2 = [
                    "Hi!",
                    "Hi mate!",
                    "What's your name?",
                    "I'm your assistant.",
                    "How old are you?",
                    "I'm 30 years old!",
                    "Why are you so mad?",
                    "Because of you!",
                    "Do you have iPhone?",
                    "Of course I do!",
                    "What's your favorite food?",
                    "I like pizze",
                    "What's your job?",
                    "I'm an assistant!",
                    "I don't know what you're talking about!"
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)
list_trainer.train(list_to_train2)

while True:
    user_response = input("User: ")
    print("Chatbot: ", bot.get_response(user_response))