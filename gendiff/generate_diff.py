"""Generate diff function."""


def json_to_text(data):
    """
    Переводит json в текст
    data: is data
    """
    diff = str(data).replace("'", '')
    diff = diff.replace('{', '{\n ')
    diff = diff.replace('}', '\n}')
    diff = diff.replace(',', '\n')
    return diff


def do_if_one_file_empty(data1, data2):
    """
    Возвращает разницу файлов, если один из файлов содержит пустой словарь
    На вход передаются пути к файлам JSON
    data1: file path,
    data2: file path
    return: diff
    """
    result = {}
    if data1 == {} or data1 is None:
        for key, value in data2.items():
            key = '+ ' + key
            result.setdefault(key, value)
        diff = json_to_text(result)
        return diff
    elif data2 == {} or data2 is None:
        for key, value in data1.items():
            key = '- ' + key
            result.setdefault(key, value)
        diff = json_to_text(result)
        return diff


def generate_diff(data1, data2):
    """
    Вычислитель отличий файлов JSON.
    На вход передаются пути к файлам JSON
    data1: file path,
    data2: file path,
    Return difference
    """
    result = {}
    if (data1 == {}) or (data2 == {}):
        return do_if_one_file_empty(data1, data2)
    elif (data1 is None) or (data2 is None):
        return do_if_one_file_empty(data1, data2)
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        if key not in data1:
            value = data2[key]
            key = f'+ {key}'
            result.setdefault(key, value)
        elif key not in data2:
            value = data1[key]
            key = f'- {key}'
            result.setdefault(key, value)
        elif data1[key] == data2[key]:
            value = data1[key]
            key = f'  {key}'
            result.setdefault(key, value)
        else:
            value1 = data1[key]
            key1 = f'- {key}'
            result.setdefault(key1, value1)
            key2 = f'+ {key}'
            value2 = data2[key]
            result.setdefault(key2, value2)
    diff = json_to_text(result)
    return diff
