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
import random
author = 'Your name here'

doc = """
This will appear before grouping. The idea is to avoid forming groups according to their speed. It will look like a loading screen.
"""


class Constants(BaseConstants):
    name_in_url = 'beforegrouping'
    players_per_group = None
    num_rounds = 1
# Set   session.configs['random_wait_min'] 
# Set   session.configs['random_wait_max'] 


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.waiting_time = random.randint(self.session.config['random_wait_min_sec'], self.session.config['random_wait_max_sec'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    waiting_time = models.IntegerField()
    timeout = models.BooleanField()
    

    def set_arrival_time(self):
        self.participant.vars['arrival_time'] = time.time()
        # this is for the next app
        



