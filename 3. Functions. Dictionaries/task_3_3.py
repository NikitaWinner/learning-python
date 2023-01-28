def thesaurus(*args) -> dict:
    """ Функция, принимает в качестве аргументов имена сотрудников
    и возвращает словарь, в котором ключи — первые буквы имён,
    а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. """

    dict_out = {}
    for name in args:
        dict_out.setdefault(name[0], [])
        if name[0] in dict_out:
            dict_out[name[0]].append(name)
    sort_dict_out = sorted(dict_out.items(), key=lambda el: el[0])
    return dict(sort_dict_out)


print(thesaurus('Муся', "Иван", "Мария", "Петр", "Илья", 'Пашган'))

def thesaurus_2(*args) -> dict:
    """ Функция, принимает в качестве аргументов имена сотрудников
    и возвращает словарь, в котором ключи — первые буквы имён,
    а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. """

    dict_out = {}
    for name in args:
        dict_out[name[0]] = list(filter(lambda el: el.startswith(name[0]), args))
    return dict(sorted(dict_out.items()))

print(thesaurus_2("Никита", 'Витя', "Слава", "Нина", "Валерия", 'Юра'))


def thesaurus_bdsm(*args) -> dict:
    """ Функция (bdsm-версия), принимает в качестве аргументов имена сотрудников
    и возвращает словарь, в котором ключи — первые буквы имён,
    а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. """
    return dict(sorted({name[0].title() : list(filter(lambda el: el[0] == name[0], args)) for name in args}.items(), key=lambda el: el[0]))
print(thesaurus_bdsm('dark','dariy', "bunny", "Puppy", "miss", "rope", 'ridic', 'Mr.Krabs'))