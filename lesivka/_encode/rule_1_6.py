# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import translator

IN, OUT = 'Ї', 'JI'

convert = translator({IN: OUT, IN.lower(): OUT.lower()})
