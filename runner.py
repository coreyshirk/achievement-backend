#!/usr/bin/env python
import os
import sys
import subprocess
import json

data = json.loads(open('.env.json', 'r').read())
for key, value in data.items():
    if isinstance(value, dict) or isinstance(value, list):
        value = json.dumps(value)
    os.environ[key] = value

try:
    # Now the new process has all the environment variables from .env.json
    result = subprocess.run(' '.join(sys.argv[1:]), shell=True)
    exit(result.returncode)
except KeyboardInterrupt:
    pass
