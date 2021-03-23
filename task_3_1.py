# задание 1
def num_translate(word):
    words = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eigth': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return words.get(word)