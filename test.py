from chatterbot import ChatBot
import spacy
import pkg_resources

nlp = spacy.load("en_core_web_sm")

bot = ChatBot('MyBot')

chatterbot_version = pkg_resources.get_distribution("chatterbot").version
print("ChatterBot version:", chatterbot_version)
