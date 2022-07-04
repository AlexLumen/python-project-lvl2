"""Generate diff function."""


def json_to_text(diff_dict):
    """

    Переводит json в текст.
    diff_dict: is data
    return: difference text
    """
    diff = str(diff_dict).replace("'", '')
    diff = diff.replace('{', '{\n ')
    diff = diff.replace('}', '\n}')
    return diff.replace(',', '\n')


def generate_diff(data1, data2):
    """

    Вычислитель отличий файлов JSON.
    На вход передаются пути к файлам JSON
    data1: file path,
    data2: file path,
    Return difference
    """
    diffed_dict = {}

    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        if key not in data1:
            value_key = data2[key]
            key = f'+ {key}'
            diffed_dict.setdefault(key, value_key)
        elif key not in data2:
            value_key = data1[key]
            key = f'- {key}'
            diffed_dict.setdefault(key, value_key)
        elif data1[key] == data2[key]:
            value_key = data1[key]
            key = f'  {key}'
            diffed_dict.setdefault(key, value_key)
        else:
            value_key1 = data1[key]
            key1 = f'- {key}'
            diffed_dict.setdefault(key1, value_key1)
            key2 = f'+ {key}'
            value_key2 = data2[key]
            diffed_dict.setdefault(key2, value_key2)
    diff = json_to_text(diffed_dict)
    return diff
