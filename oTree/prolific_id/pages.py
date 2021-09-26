from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ProlificID(Page):
    form_model = 'player'
    form_fields = ['prolific_id']


page_sequence = [ProlificID]
