import django.core.exceptions
import random

from .config import MindsightConfig
from .store import SampleStore


class Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self._config = MindsightConfig()

        if self._config.MINDSIGHT_AGENT_URL is None:
            raise django.core.exceptions.MiddleWareNotUsed

        if self._config.MINDSIGHT_SAMPLE_PROBABILITY < 0.0:
            raise django.core.exceptions.MiddleWareNotUsed

        self._store = SampleStore(
            self._config.MINDSIGHT_AGENT_URL,
            send_after=self._config.MINDSIGHT_SEND_AFTER,
            send_timeout=self._config.MINDSIGHT_SEND_TIMEOUT)


    def __call__(self, request):
        profile = False

        if self._config.MINDSIGHT_SAMPLE_PROBABILITY >= 1.0:
            profile = True
        elif random.random() < self._config.MINDSIGHT_SAMPLE_PROBABILITY:
            profile = True

        response = self.get_response(request)

        if profile is True:
            print("hit")
            self._store.record("hit")

        return response
