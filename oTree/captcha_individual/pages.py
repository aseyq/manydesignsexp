from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
import time
class Instructions1(Page):
    pass

class Instructions2(Page):
    pass

class Captcha(Page):
    def get_timeout_seconds(self):
        return self.session.config['captcha_page_timeout_seconds']

    form_model = 'player'
    form_fields = ['user_input']
    live_method = 'live_get_answer'

    def vars_for_template(self):
        return dict(
            random_file = self.player.get_random_image()
            )
#    def before_next_page(self):
#        self.player.asses_the_answer()

    def before_next_page(self):
        self.player.calculate_payoffs()


class Results(Page):
    form_model = 'player'
    form_fields = ["comments"]
page_sequence = [Instructions1, Instructions2, Captcha, Results]
