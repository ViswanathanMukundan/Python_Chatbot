import nltk
from nltk.chat.util import Chat, reflections
from mypkg.setpairs import set_pairs

chat = Chat(set_pairs, reflections)
chat.converse()
