# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat):

    quantity = 1
    joke_array = []
    while quantity <= n:
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        # Повторяться можно,если repeat = 1. Если отлично от 1 - то нельзя
        if repeat == 1:
            joke_array.append(f'{noun} {adverb} {adjective}')
            quantity += 1
        else:
            joke_array.append(f'{noun} {adverb} {adjective}')
            nouns.pop(nouns.index(noun))
            adverbs.pop(adverbs.index(adverb))
            adjectives.pop(adjectives.index(adjective))
            quantity += 1
            if len(nouns) == 0:
                break

    return joke_array


print(get_jokes(6, 1))
