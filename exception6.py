try:
    import HomeWork2
except ModuleNotFoundError:
    print('Нет такая модуль!')
except SyntaxError:
    print('Напишите имя модуля или напишите правильно имя модуля!')
try:
    seq = HomeWork2.seq_record.seq
except AttributeError:
    print('Object has no attribute!')
except SyntaxError:
    print('Invalid syntax!')


table = 1
min_pro_len = 100
try:
    for strand, nuc in [(+1, seq), (-1, seq.reverse_complement())]:
        for frame in range(3):
            for pro in nuc[frame:].translate(table).split("*"):
                if len(pro) >= min_pro_len:
                    print ("%s...%s - length %i, strand %i, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))
except Exception:
    print('Есть исключение в коде!')
finally:
    print("The End")
print(len(seq))