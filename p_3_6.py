def int_func():
    a = input('Введите английские слова, разделенные пробелами ').split()
    for word in a:
        let = 0
        for letter in word:
            if 97 <= ord(letter) <= 122:
                let += 1
        if let == len(word):
            print(word.title())
        else:
            print(f'Пожалуйста, используйте строчные буквы')

int_func()