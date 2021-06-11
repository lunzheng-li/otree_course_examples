from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction(Page):
    timeout_seconds = 1200

    def is_displayed(self):
        return self.player.round_number == 1
    pass


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    body_text = "We are waiting for everyone to finish. \
                Thank you so much for your patience."
    pass


class Results(Page):
    def vars_for_template(self):
        a = self.group.total_contribution * Constants.factor
        return dict(total_earnings=a)

    def before_next_page(self):
        if self.player.round_number == Constants.num_rounds:
            player = self.player
            player.set_final_payoffs()
    pass


class Final(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass


page_sequence = [
    Instruction,
    Contribute,
    ResultsWaitPage,
    Results,
    Final,
]
