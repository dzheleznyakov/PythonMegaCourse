import os
import json
from difflib import get_close_matches

data_path = 'data/data.json'
if os.path.exists(data_path):
    with open(data_path) as file:
        data = json.load(file)
else:
    data = {}

not_found_message = "The word doesn't exist. Please double check it."


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    if w.title() in data:
        return data[w.title()]

    if w.upper() in data:
        return data[w.upper()]

    matches = get_close_matches(w, data.keys(), cutoff=0.8)
    if len(matches) == 0:
        return not_found_message

    best_match = matches[0]
    yn = input("Did you mean '%s' instead? Enter Y if yes, or N if no: " % best_match)
    if yn.upper() == "Y":
        return data[best_match]
    elif yn.upper() == "N":
        return not_found_message
    else:
        return "We didn't understand your entry."


while True:
    word = input("Enter word (enter '\\exit' to finish): ")
    if word == "\\exit":
        break
    translation = translate(word)
    if type(translation) == list:
        for definition in translation:
            print("* %s" % definition)
    else:
        print("* %s" % translation)
