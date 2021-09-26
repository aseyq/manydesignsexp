from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_fields = ['takeaway']
    form_model = "player"

page_sequence = [Decision]
