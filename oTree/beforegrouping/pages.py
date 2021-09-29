from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Loading(Page):
    def js_vars(self):
        return dict(waiting_time=self.player.waiting_time)

    def before_next_page(self):
        self.player.set_arrival_time()


page_sequence = [Loading]
