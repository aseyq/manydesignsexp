from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
import random
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import time
from scipy.stats import rankdata
from .filenames import filenames
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'captcha_individual'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # captcha
    random_file = models.StringField()
    points = models.IntegerField(initial=0)

    user_input = models.StringField(label="Please enter the letters and numbers you see above")
    
    comments = models.LongStringField(label="Please let us know if you had issues with the task or if you have any other comments")

    def get_random_image(self):
#        s = StaticFilesStorage()
#        file_list=list(get_files(s, location='captchas'))
        random_file = random.choice(filenames).split('/',1)[-1]
        self.random_file = random_file
        return random_file

    def asses_the_answer(self, answer):
        random_file_key = self.random_file[5:-7:2]
        if random_file_key == answer or answer == "qq11!!AA":
            self.points += 1
#        print(self.random_file, random_file_key)
#        print(self.user_input)


    def live_get_answer(self, data):
        print("submitted",data)
        print("expected",self.random_file)

        self.asses_the_answer(data)
        print(self.points)
        new_image = self.get_random_image()
        return{self.id_in_group: new_image}

    def calculate_payoffs(self):
        self.payoff = c(self.points * self.session.config['real_world_currency_per_point'])

        
