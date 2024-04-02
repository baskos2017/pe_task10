import re 
def tex_tanalyzer(text):
    words = re.split(r'\s', text)
    unique_words = set(words)

    print('Унікальні слова:')
    for word in unique_words:
        print(word)

    total_words = len(words)
    unique_word_count = len(unique_words)

    print('Загальна кількість слів:', total_words)
    print('Кількість унікальних слів:', unique_word_count)

text = input('Введіть текст слова розділіть пробілами: ')
tex_tanalyzer(text)
