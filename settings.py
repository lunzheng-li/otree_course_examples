from os import environ

SESSION_CONFIGS = [
    dict(
        name='public_goods',
        display_name="Econ6053 - Public Goods Game",
        num_demo_participants=3,
        app_sequence=['econ6053_pgg', ]
    ),
    dict(
        name='public_goods_treatments',
        display_name="Econ6053 - Public Goods Game - two treatments",
        num_demo_participants=6,
        app_sequence=['econ6053_pgg_treatments', ]
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'opg=ws&wh@6e!c*29@x29su)*l0xw6xoieu0i3+*-)vih-=t8-'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
