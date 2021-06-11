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

import random

author = 'Lunzheng Li'

doc = """
A public goods game
- three participants
- initial endowment 20 pounds
- factor: 1.2
"""


class Constants(BaseConstants):
    name_in_url = 'econ6053_pgg'
    players_per_group = 3
    num_rounds = 3

    endowment = c(20)
    factor = 1.2

    instructions_template = 'econ6053_pgg/Instruction_temp.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            if self.round_number == Constants.num_rounds:
                p.paying_round = random.randint(1, Constants.num_rounds)
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum(
            [p.contribution for p in self.get_players()])
        self.individual_share = (self.total_contribution * Constants.factor
                                 / Constants.players_per_group)
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribution) + \
                self.individual_share
    pass


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        label="How much will you contribute to the project (from 0 to 20)?"
    )
    paying_round = models.IntegerField()
    final_payoff = models.CurrencyField()

    def set_final_payoffs(self):
        self.final_payoff = self.in_round(self.paying_round).payoff
    pass
