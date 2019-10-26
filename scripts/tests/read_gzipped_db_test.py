import gzip
from Bio import SeqIO
#TODO add todo to every file to add their imports to a list of
# depenencies


# bighelp from https://stackoverflow.com/questions/42757283/seqio-parse-on-a-fasta-gz


gzip_db_location = "/home/queue/SwissProt/uniprot_trembl.fasta.gz"

# gzip doc on modes https://docs.python.org/3/library/functions.html#open
# "rt" means "read text"? i think?

mi, ma = 25, 0
with gzip.open(gzip_db_location, 'rt') as db_as_zipfile:
    testcount = 0
    for i, seqio_record in enumerate( SeqIO.parse(db_as_zipfile, "fasta")):

        if len(seqio_record.id) < mi:
            mi = len(seqio_record.id)
        if len(seqio_record) > ma:
            ma = len(seqio_record.id)

        if i % 1000000 == 0:
            print(i)

print(mi, ma)


                

                    
