from setuptools import setup


setup(
    name="mindsight-django",
    version="0.1",
    description="Mindsight HotPath Sampler for Python/Django",
    url="https://github.com/MindsightCo/mindsight-django-hotpath",
    license="Apache 2.0",
    packages=["mindsight_django"],
    install_requires=["requests", "django"]
)
