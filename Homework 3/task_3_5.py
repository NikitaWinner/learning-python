import random


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count
    :param count: int колчество шуток, которое нужно вернуть
    :return: список строк """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_out = []
    for i in range(count):
        list_words = list(map(random.choice, [nouns, adverbs, adjectives]))
        list_out.append(' '.join(list_words))
    return list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
print('\n \n')
def get_jokes_adv(count: int, repeat=False) -> list:
    """Возвращает список шуток в количестве count
        :param count: int колчество шуток, которое нужно вернуть
        :return: список строк
        Keyword arguments:
            repeat -- флаг, который определяет можно повторять слова в шутках или нет (default 0.0)"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_out = []
    if not repeat:
        a = len(adjectives)
        b = len(adverbs)
        c = len(nouns)
        d = count
        count = min(len(adjectives), len(adverbs), len(nouns), count)
    for i in range(count):
        if repeat:
            return get_jokes(count)
        else:
            result = list(map(lambda x: x.pop(random.randrange(len(x))), [nouns, adverbs, adjectives]))
            list_out.append(' '.join(result))
    return list_out


print(get_jokes_adv(2))
print(get_jokes_adv(15))