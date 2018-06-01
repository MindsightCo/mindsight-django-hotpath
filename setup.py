import sys
from setuptools import setup

install_requires = ["requests", "django"]
if sys.version_info[:2] < (3, 4):
    install_requires.append('pathlib')

setup(
    name="mindsight-django-hotpath",
    version="0.3",
    description="Mindsight Collector for Python/Django",
    url="https://github.com/MindsightCo/mindsight-django-hotpath",
    license="Apache 2.0",
    packages=["mindsight_django"],
    install_requires=install_requires
)
