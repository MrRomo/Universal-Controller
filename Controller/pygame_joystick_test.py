import json
from Control import Control

data = []
with open('buttons.json') as json_file:
    data = json.load(json_file)

control = Control(data)


