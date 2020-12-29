# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:36:01 2020

@author: Andreas Perpyrakis
first attemnt of creating a chat-bot named Jack plus using Git
"""
'''
before use chat bot make sure you have installed these:
pip install --upgrade pip
pip install chatterbot
pip install chatterbot-corpus
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name='Jack', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

#standarized answers
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)


for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item) 

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print (my_bot.get_response("Hi there"))
print (my_bot.get_response("I had a nice day"))
print (my_bot.get_response("What's your name stranger?"))
print (my_bot.get_response("Use Pythagorean Theorem "))
print (my_bot.get_response("Show me Law of Cosines"))

while True:
    try:
        bot_input = input("You ")
        bot_response = my_bot.get_response(bot_input)
        print (f"{my_bot.name}: {bot_response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    