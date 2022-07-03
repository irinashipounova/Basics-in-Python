with open('new_file.txt', 'w', encoding='utf-8') as n_f:

    dt = " "
    while dt:
        dt = input('Enter your data: ')
        n_f.write(f"{dt}\n") if dt != '' else n_f.close
