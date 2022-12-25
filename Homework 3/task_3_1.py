def num_translate(value: str) -> str:
    """переводит числительное от 0 до 10 с английского на русский"""
    translator = {
        'one': 'один', 'six': 'два',
        'two': 'три', 'seven': 'четыре',
        'three': 'пять', 'eight': 'шесть',
        'four': 'семь', 'nine': 'восемь',
        'five': 'девять', 'ten': 'десять',
    }
    str_out = translator.get(value)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
