new_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as text:
    for line in text:
        lesson_timing = []
        lessons = ([el for el in line.split(" ")])
        for el in lessons:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        new_dict[line.split(':')[0]] = sum([int(i) for i in lesson_timing if i.isdigit()])

print(new_dict)
