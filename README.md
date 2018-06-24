# Mindsight Data Collector for Python's Django Web Framework

This utility can be plugged in to your Django application to collect vital data about your code's behavior so that Mindsight can help you write better code more safely.

## Installation

The latest production-ready version of this utility is distributed via PyPI and can be installed as follows:

```
pip install mindsight-django-hotpath
```

## Configuration

This utility runs as a Django middleware in your application. To configure it add the following to your `settings.py` file:

```python
import mindsight_django

# rest of your configuration

# Mindsight collector config

# URL where you are running the Mindsight Agent
MINDSIGHT_AGENT_URL = 'http://localhost:8000'

# Name of your project as configured in Mindsight
MINDSIGHT_PROJECT = 'my-project-name'
```

The `MINDSIGHT_AGENT_URL` setting is the URL of the [Mindsight Agent](https://github.com/MindsightCo/hotpath-agent), which is
required to send diagnostic data to Mindsight's backend for further analysis. If this setting is omitted, Mindsight's middleware will be disabled by the Django runtime.

The `MINDSIGHT_PROJECT` setting is the name of your project you've configured in the Mindsight service. If this setting is omitted, Mindsight's middleware will be disabled by the Django runtime.

Finally, register Mindsight as a Django middleware in your `settings.py` file:

```python
MIDDLEWARE = [
  # ... other middlewares
  'mindsight_django.Middleware',  # should be the last middleware
]
```

To ensure the highest quality data to better analyze your application with, the Mindsight middleware should be the last one to run.

## Fine-Tuning (Optional)

The Mindsight middleware has additional configuration options to fine-tune its behavior. The defaults should be desirable for most applications, but they can be tweaked if needed:

### Options

- `MINDSIGHT_ENVIRONMENT`
  - Default: `'production'`
  - Deployment environment your program is running in. Change this if you have multiple environments you want to measure independently.
- `MINDSIGHT_SEND_AFTER`
  - Default: `100`
  - Number of measurements to cache before sending data to the [Mindsight Agent](https://github.com/MindsightCo/hotpath-agent).
- `MINDSIGHT_SEND_TIMEOUT`
  - Default: `0.05`
  - Amount of time (seconds) to wait for a response from the [Mindsight Agent](https://github.com/MindsightCo/hotpath-agent) when sending measurements. An error will be logged in case of communication failure with the agent.
- `MINDSIGHT_SAMPLE_PROBABILITY`
  - Default: `0.02`
  - Probability that a request will be intercepted and analyzed by Mindsight.
- `MINDSIGHT_SAMPLE_INTERVAL`
  - Default: `0.010`
  - Simulates the behavior of a sampling profiler that interrupts the application every 10ms.
