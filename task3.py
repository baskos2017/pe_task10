import re

def last_three_symbols():
    
    result = re.findall(r'\w{3}\b', words)
    print(result)

words = input('Введіть слова довжиною більше 3 символів:\n')
if len(words) < 3:
    print('Довжина слова повинна бути більше 3 символів')
else:
        last_three_symbols()
