from setuptools import setup


setup(
    name="mindsight-django-hotpath",
    version="0.3.2",
    description="Mindsight Collector for Python/Django",
    url="https://github.com/MindsightCo/mindsight-django-hotpath",
    license="Apache 2.0",
    packages=["mindsight_django"],
    install_requires=[
        "requests",
        "django",
        'pathlib;python_version<"3.4"',
    ]
)
