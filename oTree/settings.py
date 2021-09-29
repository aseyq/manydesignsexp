from os import environ


common_app_sequence = [
#    'prolific_id', 
#    'instructions',
    'beforegrouping',
#    'grouping', ## REMOVED
    'captcha', 
#    'decision', ## REMOVED
    'notmatched',
    'prolific_redirect',
    'timeoutblock',
]

# Parameters - Also should be added to SESSION_CONFIGS or SESSION_CONFIG_DEFAULTS
completion_url = "https://app.prolific.co/submissions/complete?cc=572FB13C"
matching_timeout_mins = 5
random_wait_min_sec = 1
random_wait_max_sec = 3
showup_fee = 1.30
currency_conversion = 0.1

SESSION_CONFIGS = [
    dict(
        name='manydesigns_comp',
        display_name="ManyDesigns Treatment - Competition",
        competition=True,
        num_demo_participants=12,
        app_sequence=common_app_sequence,
    ),
    dict(
        name='manydesigns_nocomp',
        display_name="ManyDesigns Treatment - Control",
        competition=False,
        app_sequence=common_app_sequence,

    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=currency_conversion, 
    participation_fee=0.00, 
    doc="",
    num_demo_participants=12,
    completion_url=completion_url,
    matching_timeout_mins = matching_timeout_mins,
    random_wait_min_sec = random_wait_min_sec,
    random_wait_max_sec = random_wait_max_sec,
    showup_fee = showup_fee,
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

SECRET_KEY = '!0(z^*=gbdeg1uce+tbg(zfdo81hc3p@&2d(5f7&4wc&96t52e'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
#RANDOM_IMAGE_DIR = "captchas/"
