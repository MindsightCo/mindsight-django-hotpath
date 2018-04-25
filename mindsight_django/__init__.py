import cProfile
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


    def _must_profile(self):
        if self._config.MINDSIGHT_SAMPLE_PROBABILITY >= 1.0:
            return True
        elif random.random() < self._config.MINDSIGHT_SAMPLE_PROBABILITY:
            return True

        return False



    def __call__(self, request):
        profiler = None

        if self._must_profile():
            profiler = cProfile.Profile()
            profiler.enable()
        
        response = self.get_response(request)

        if profiler is not None:
            profiler.disable()
            profiler.print_stats(sort="time")
            self._store.record("hit")

        return response
