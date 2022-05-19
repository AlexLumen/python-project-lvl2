"""Generate diff function."""
#import json

#import yaml


def generate_diff(file1, file2):
    """
    Вычислитель отличий файлов JSON.
    На вход передаются пути к файлам JSON
    file1: file path,
    file2: file path,
    Return difference
    """
    diff_dict = {}

    if file1 is None and file2 is None:
        return '{\n\n}'

    elif file1 == {} or file1 is None:
        print(type(file1))
        for key, val in file2.items():
            key = '+ ' + key
            diff_dict.setdefault(key, val)
    elif file2 == {} or file2 is None:
        for key, val in file1.items():
            key = '- ' + key
            diff_dict.setdefault(key, val)

    else:
        for key, value in file1.items():
            for k, v in file2.items():
                if key == k:
                    if value != v:
                        new_key = '- ' + key
                        diff_dict.setdefault(new_key, value)
                        new_key = '+ ' + key
                        value = v
                        diff_dict.setdefault(new_key, value)
                    else:
                        new_key = '  ' + key
                        diff_dict.setdefault(new_key, value)
                if key not in file2:
                    key = '- ' + key
                    diff_dict.setdefault(key, value)
                    break
                if k not in file1:
                    k = ' + ' + k
                    diff_dict.setdefault(k, v)
    diff = str(diff_dict).replace("'", '')
    diff = diff.replace('{', '{\n')
    diff = diff.replace('}', '\n}')
    diff = diff.replace(',', '\n')

    return diff


#file_path_1 = yaml.load(open('../../fixtures/file1.yaml'))
#file_path_2 = yaml.load(open('../../fixtures/file2.yaml'))
#print(type(file_path_1))
#print(type(file_path_2))

#print(generate_diff(file_path_1, file_path_2))
#print(type(generate_diff(file_path_1, file_path_2)))
