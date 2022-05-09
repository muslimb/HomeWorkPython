from Bio.Seq import Seq
import HomeWork2

seq = HomeWork2.seq_record.seq

table = 1
min_pro_len = 100

for strand, nuc in [(+1, seq), (-1, seq.reverse_complement())]:
    for frame in range(3):
        for pro in nuc[frame:].translate(table).split("*"):
            if len(pro) >= min_pro_len:
                print ("%s...%s - length %i, strand %i, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))

print(len(seq))