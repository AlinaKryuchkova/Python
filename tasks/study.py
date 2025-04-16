def truncate(text, length):
    return text[:length] + '...'


print(truncate('hexlet', 3))

def traer(card, star=4):
    newCard = card[:star]
    newStar = str.replace('*', newCard)


def trim_and_repeat(text, offset=0, repetitions=1):
    newText = text[offset:]
    return newText * repetitions

print(trim_and_repeat('python', offset=3, repetitions=2))

def letter_multiply(word: str, letter: str, num: int) -> str:
    newLetter = letter*num
    if letter in word:
        return word.replace(letter, newLetter)
print(letter_multiply('python', 'p', 2))

def get_age_difference(burn_one: int, burn_two: int):
    return abs(burn_one - burn_two)
actual = get_age_difference(2018, 2021)
print(actual)

def  string_or_not(text):
    if isinstance(text, str):
        print('yes')
    else:
        print('no')

print(string_or_not(None))

def normalize_url(adress: str):
    if adress.startswith('http://'):
        start = adress[7:]
        return 'https://' + start
    elif not adress.startswith('http://') and not adress.startswith('https://'):
        return 'https://' + adress
    else:
        return adress
print(normalize_url('https://gogole'))
