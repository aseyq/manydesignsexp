from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
import time
class Grouping(WaitPage):
    after_all_players_arrive = "assign_names_group"
    title_text = "Please stay on this screen - The tasks will start soon"
    body_text = ""

    group_by_arrival_time = True
    template_name = 'captcha/Grouping.html'

    def app_after_this_page(self, upcoming_apps):

        if self.player.waiting_too_long():
            return "notmatched"

    def js_vars(self):
        return dict(arrival_time=self.participant.vars['arrival_time'], current_time=time.time(),timeout_mins=self.session.config['matching_timeout_mins'])

    def before_next_page(self):
        print("names are assigning")
        self.player.assign_names()


class Captcha(Page):
#    timeout_seconds = 240
    timeout_seconds = 60 * 1

    form_model = 'player'
    form_fields = ['user_input']
    live_method = 'live_get_answer'

    def vars_for_template(self):
        return dict(
            random_file = self.player.get_random_image()
            )
#    def before_next_page(self):
#        self.player.asses_the_answer()


class Decision(Page):
    form_fields = ['takeaway']
    form_model = "player"

class ResultsWait(WaitPage):
    after_all_players_arrive = "calculate_payoffs"

class Results(Page):
    def vars_for_template(self):
        ranked = self.group.get_performance_data_ranked()
        alph = self.group.get_performance_data_alph()

        return dict(ranked=ranked, alph=alph)


page_sequence = [Grouping, Captcha, Decision, ResultsWait, Results]
