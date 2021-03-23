# задание 5.
import random
nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
def get_jokes(n):
    """Генератор шуток из списков"""
    for i in range(n):
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
    words = random.choice(nouns)
    words2 = random.choice(adverbs)
    words3 = random.choice(adjectives)
    return words, words2, words3
print(get_jokes(n=1))