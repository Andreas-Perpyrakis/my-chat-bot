# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:36:01 2020

@author: Andreas Perpyrakis
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

