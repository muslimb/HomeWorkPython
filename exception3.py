try:
    import re
    from Bio import SeqIO
except ModuleNotFoundError:
    print('Нет такая модуль!')
except SyntaxError:
    print('Напишите имя модуля или напишите правильно имя модуля!')
try:
    file = open(input('Напишите имя файла на формате фаста: '))
except FileNotFoundError:
    print('Нет такой файл!')
primer1 = input('1-ый праймер: ')
primer2 = input('2-ой праймер: ')
try:
    for seq_record in SeqIO.parse(file, "fasta"):
        seq_record.seq
except UnicodeDecodeError:
    print('Это файл не формате фаста!')
except FileNotFoundError:
    print('Нет такой файл!')

a = seq_record.seq
c = str(a)

class Otveti():
    def primer1(self):
        print('Анализ ответов для 1ый праймер: ')
        try:
            for obj in enumerate(re.finditer(primer1, c)):
                print('%d | %2d-%2d: %s' % (obj[0], obj[1].start(), obj[1].end(), obj[1].group(0)))
        except NameError:
            print('Укажите правильно шаблона который хотите найти! В 1ом праймире!')


    def primer2(self):
        print('Анализ ответов для 2ой праймер: ')
        try:
            for obj in enumerate(re.finditer(primer2, c)):
                print('%d | %2d-%2d: %s' % (obj[0], obj[1].start(), obj[1].end(), obj[1].group(0)))
        except NameError:
            print('Укажите правильно шаблона который хотите найти! В 2ом праймире!')

m = Otveti()
m.primer1()