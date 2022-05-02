from Bio import SeqIO
import pandas as pd
for seq_record in SeqIO.parse("sequence (2).fasta", "fasta"):
    seq_record.name
    seq_record.seq

a = seq_record.name
b = len(seq_record.seq)
c = (seq_record.seq.count('A') / b) * 100
d = (seq_record.seq.count('T') / b) * 100
e = (seq_record.seq.count('G') / b) * 100
f = (seq_record.seq.count('C') / b) * 100
print(c, d, e, f)

df = pd.DataFrame({'Name' : [a], 'Lenght' : [b], 'Частота A: ' : [c], 'Частота T: ' : [d], 'Частота C: ' : [f], 'Частота G: ' : [e]})
print(df)

df.to_excel('muslimbek.xlsx')






