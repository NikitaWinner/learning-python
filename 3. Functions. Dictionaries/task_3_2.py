def num_translate_adv(value: str) -> str:
    """переводит числительное от 0 до 10 с английского на русский
    учитываю регистр первой буквы"""

    translator = {
        'one': 'один', 'six': 'два',
        'two': 'три', 'seven': 'четыре',
        'three': 'пять', 'eight': 'шесть',
        'four': 'семь', 'nine': 'восемь',
        'five': 'девять', 'ten': 'десять',
    }
    str_out = translator.get(value.lower())
    return str_out.title()


print(num_translate_adv("One"))
print(num_translate_adv("eight"))