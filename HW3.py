import re
from Bio import SeqIO
file = open(input('Напишите имя файла на формате фаста: '))
primer1 = input('1-ый праймер: ')
primer2 = input('2-ой праймер: ')
for seq_record in SeqIO.parse(file, "fasta"):
    seq_record.seq

a = seq_record.seq
c = str(a)

class Otveti():
    def primer1(self):
        self.fil = file
        print('Анализ ответов для 1ый праймер: ')
        for obj in enumerate(re.finditer(primer1, c)):
            print('%d | %2d-%2d: %s' % (obj[0], obj[1].start(), obj[1].end(), obj[1].group(0)))

    def primer2(self):
        print('Анализ ответов для 2ой праймер: ')
        for obj in enumerate(re.finditer(primer2, c)):
            print('%d | %2d-%2d: %s' % (obj[0], obj[1].start(), obj[1].end(), obj[1].group(0)))


m = Otveti()
m.primer1()
m.primer2()




