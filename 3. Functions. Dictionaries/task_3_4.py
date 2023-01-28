def thesaurus_adv(*args) -> dict:
    """ Функция, принимает в качестве аргументов строки в формате «Имя Фамилия»
    и возвращающает словарь, в котором ключи — первые буквы фамилий,
    а значения — словари, в котором ключи — первые буквы имён, а их
    значения — списки, содержащие имена, начинающиеся с соответствующей буквы. """

    dict_out = {}
    for i in range(len(args)):
        list_name = args[i].split()
        let_name, let_pat = list_name[0][0], list_name[1][0]
        dict_out.setdefault(let_pat, {})
        if let_pat in dict_out:
            dict_out[let_pat].setdefault(let_name, [])
            if let_name in dict_out[let_pat]:
                dict_out[let_pat][let_name].append(args[i])
    sort_dict_out = sorted(dict_out.items(), key=lambda el: el[0])
    return dict(sort_dict_out)


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))