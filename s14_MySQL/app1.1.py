import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()


def query(w=None, pos=1):
    if w == "" or w is None:
        cursor.execute("SELECT * FROM Dictionary")
    else:
        cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'" % w)
    results = cursor.fetchall()
    return [result[pos] for result in results]


not_found_message = "The word doesn't exist. Please double check it."


def translate(w):
    w = w.lower()
    data = query(w)
    if data:
        return data

    w_titled = w.title()
    data = query(w_titled)
    if data:
        return data

    w_upper = w.upper()
    data = query(w_upper)
    if data:
        return data

    data = query(pos=0)
    matches = get_close_matches(w, data, cutoff=0.8)
    if len(matches) == 0:
        return not_found_message

    best_match = matches[0]
    yn = input("Did you mean '%s' instead? Enter Y if yes, or N if no: " % best_match)
    if yn.upper() == "Y":
        return translate(best_match)
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
        print(translation)
