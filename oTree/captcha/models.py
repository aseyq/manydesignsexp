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
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'captcha'
    players_per_group = 4
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.competition = self.session.config['competition']

    def group_by_arrival_time_method(self, waiting_players):
        num_waiting = len(waiting_players)
        self.session.vars['num_waiting'] = num_waiting
        print("number of waiting players:", self.session.vars['num_waiting'], " ", time.strftime('%X %x %Z'))
        if len(waiting_players) >= Constants.players_per_group:
            print("creating group")
            return waiting_players[:Constants.players_per_group]
        for p in waiting_players:
            if p.waiting_too_long():
                return [p]



class Group(BaseGroup):
    # decision
    selected_id_in_group = models.IntegerField()
    selected_takeaway = models.IntegerField()

    def calculate_payoffs(self):


        # selecting the dictator
        self.selected_id_in_group = random.choice(range(1,Constants.players_per_group+1))
        self.selected_takeaway = self.get_player_by_id(self.selected_id_in_group).takeaway

        players_in_group = self.get_players() # ordered by id in group but doublecheck

        for p in players_in_group:
            p.is_dictator = True if p.id_in_group == self.selected_id_in_group else False

        # rank calculation

        points = [p.points + random.uniform(0,0.5) for p in players_in_group]
        ranks = len(points) +1 - rankdata(points)

        for p in players_in_group:
            p.my_rank = ranks[p.id_in_group-1]




class Player(BasePlayer):
    # captcha
    random_file = models.StringField()
    points = models.IntegerField(initial=0)
    user_input = models.StringField(label="Please enter the letters and numbers you see above")

    # decision
    competition = models.BooleanField()
    takeaway = models.IntegerField()
    is_dictator = models.BooleanField()

    # results
    my_rank = models.IntegerField()

    def get_random_image(self):
        s = StaticFilesStorage()
        file_list=list(get_files(s, location='captchas'))
        random_file = random.choice(file_list).split('/',1)[-1]
        self.random_file = random_file
        return random_file

    def asses_the_answer(self, answer):
        random_file_key = self.random_file[5:-7:2]
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


    def waiting_too_long(self):
        return time.time() - self.participant.vars['arrival_time'] > self.session.config['matching_timeout_mins'] * 60


        
