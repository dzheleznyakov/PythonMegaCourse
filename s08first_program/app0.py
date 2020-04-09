wh_words = ['What', 'Who', 'Which', 'How', 'Whom']
punctuations = ['.', '?', '!']


def is_question(phrase):
    for wh_word in wh_words:
        if phrase.startswith(wh_word):
            return True
    return False


def ends_with_punctuation(phrase):
    last_char = phrase[-1]
    for p in punctuations:
        if last_char == p:
            return True
    return False


def get_punctuation(phrase):
    if ends_with_punctuation(phrase):
        return ''
    elif is_question (phrase):
        return '?'
    return '.'


sentence = ''

results = []

while True:
    sentence = input('Say something: ').strip().capitalize()
    if sentence == '\end':
        break
    punctuation = get_punctuation(sentence)
    results.append("%s%s " % (sentence, punctuation))


output = ' '.join(results)
print(output)
