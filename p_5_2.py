with open('new_file_5_2.txt', 'r') as nf_52:
    text = nf_52.readlines()
    for ind, el in enumerate(text, 1):
        word = len(el.split())
        print(f'Строка {ind} содержит {word} слов')