import re
from collections import Counter

def find_frequency(text):
    words = re.findall(r'\w+', text.lower())
    
    my_counts = Counter(words)

    return my_counts


text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur\
    cursus ultricies odio, at aliquet orci lacinia vel. Suspendisse eget \
    diam nec lectus faucibus pellentesque rutrum tincidunt massa. Morbi\
    ultricies iaculis mi at laoreet. Aenean a imperdiet justo, sit amet \
    volutpat sem. Nulla at lobortis sem. Maecenas congue sagittis semper.\
    Vivamus porta sem turpis, at consectetur sapien porttitor vel. Nullam \
    hendrerit ultricies diam ultricies sollicitudin. Cras feugiat lacus vitae\
    lobortis ultricies. Morbi consequat ullamcorper magna.'
my_frequency = find_frequency(text)
print(my_frequency)

