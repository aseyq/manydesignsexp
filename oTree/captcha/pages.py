from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class MyPage(Page):
    form_model = 'player'
    form_fields = ['user_input']
    live_method = 'live_get_answer'

    def vars_for_template(self):
        return dict(
            random_file = self.player.get_random_image()
            )
    def before_next_page(self):
        self.player.asses_the_answer()



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
