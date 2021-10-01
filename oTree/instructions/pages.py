from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def get_timeout_seconds(self):
        return self.session.config['instructions_page_timeout_seconds']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.timeout:
            return "timeoutblock"



page_sequence = [Instructions]
