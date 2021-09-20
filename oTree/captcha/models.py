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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'captcha'
    players_per_group = None
    num_rounds = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    random_file = models.StringField()
    points = models.IntegerField(initial=0)
    user_input = models.StringField(label="Please enter the letters and numbers you see above")
    def get_random_image(self):
        s = StaticFilesStorage()
        file_list=list(get_files(s, location='captchas'))
        random_file = random.choice(file_list).split('/',1)[-1]
        self.random_file = random_file
        return random_file

    def asses_the_answer(self, answer):
        random_file_key = self.random_file[1:-3:2]
        if random_file_key == answer:
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

        
