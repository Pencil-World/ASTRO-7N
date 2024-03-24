from functions import setup
import json

with open('settings.json', 'r') as f:
  data = json.load(f)
# print(setup(2))
print()