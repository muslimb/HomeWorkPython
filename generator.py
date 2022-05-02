from Bio.SeqIO import parse
file = open('sequence (2).fasta')
records = parse(file, 'fasta')
for record in records:
    print([i for i in record.seq])




#a = [i for i in record]
#for c in a:
    #print(c)



