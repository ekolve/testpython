#!/usr/bin/env python

import time
import sys
import os

from pprint import pprint
pprint(dict(os.environ))
for i in range(3):
    print('.', end='')
    sys.stdout.flush()
    time.sleep(5)

