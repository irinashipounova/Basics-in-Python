eng_ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4.txt', 'r', encoding='utf-8') as text:
    with open('text_4_tr.txt', 'w', encoding='utf-8') as text_tr:
        text_tr.writelines([line.replace(line.split()[0], eng_ru_dict.get(line.split()[0])) for line in text])

