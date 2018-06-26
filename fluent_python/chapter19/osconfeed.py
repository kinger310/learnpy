#%%
# BEGIN OSCONFEED
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)  # <1>
        with urlopen(URL) as remote, open(JSON, 'wb') as local:  # <2>
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)  # <3>
#%%
feed = load()  # <1>
sorted(feed['Schedule'].keys())
len(feed['Schedule']['speakers'])
