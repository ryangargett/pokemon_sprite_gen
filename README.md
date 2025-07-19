# Simple inference harness for pokemon sprite generation

## Setup
1. install python: https://www.python.org/downloads/ and open cmd in folder
1. run `pip install -r requirements.txt`
2. run `python ./scripts/setup.py`

## Usage
`python ./scripts/main.py PROMPT`

## Prompt Engineering
In general you want to seperate *ideas* by comma separation, as the model tends to respond better. In general the more specific the better / more coherent the output.
❌ witch with glasses
✅ 1girl, glasses, witch, hat, blue flame

some modifiers have also been included, but I'd suggest playing around with them as well (anything pokemon aligned).
