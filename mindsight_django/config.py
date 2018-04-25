from copy import copy


class MindsightConfig(object):
    defaults = {
        'MINDSIGHT_SAMPLE_PROBABILITY': 0.05,
        'MINDSIGHT_SEND_AFTER': 100,
        'MINDSIGHT_SEND_TIMEOUT': 0.05
    }


    def __init__(self):
        self._setup()


    def _setup(self):
        from django.conf import settings

        options = {option: getattr(settings, option) for option in dir(settings) if option.startswith('MINDSIGHT')}
        self.attrs = copy(self.defaults)
        self.attrs.update(options)


    def __getattr__(self, item):
        return self.attrs.get(item, None)


    def __setattribute__(self, key, value):
        self.attrs[key] = value