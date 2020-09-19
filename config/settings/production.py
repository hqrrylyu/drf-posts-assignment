# flake8: noqa: W403
from .base import *

DATABASES["default"]["CONN_MAX_AGE"] = 50
