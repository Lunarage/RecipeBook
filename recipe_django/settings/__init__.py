# -*- coding: utf8 -*-

from recipe_django.settings.base import *

try:
    from recipe_django.settings.local import *
except ImportError as e:
    raise ImportError("Couldn't load local settings")
