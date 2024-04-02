import re

def dict_data(string):

    pattern = r"([a-zA-Z]+)+\s+([a-zA-Z]+)\s(\d{2}.\d{2}.\d{4}+)\s\
        ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\s(\d+)"
    result = re.match (pattern, string)
    data = {
        'Прізвище': result.group(1),
        'Ім\'я' : result.group(2),
        'Дата народження' : result.group(3),
        'Електронна адреса' : result.group(4),
        'Відгук про курси': result.group(5) 
        }
    return data


string = input('Введіть прізвище, ім\'я, дату народження, електронну адресу\
            та відгук про курси(цифрову оцінку) поля відокремлюйти пробілом: ')
result = dict_data(string)
print(result)

