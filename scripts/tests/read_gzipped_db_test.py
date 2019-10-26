import gzip
from Bio import SeqIO
#TODO add todo to every file to add their imports to a list of
# depenencies


# bighelp from https://stackoverflow.com/questions/42757283/seqio-parse-on-a-fasta-gz


gzip_db_location = "/home/queue/SwissProt/uniprot_trembl.fasta.gz"

# gzip doc on modes https://docs.python.org/3/library/functions.html#open
# "rt" means "read text"? i think?
with gzip.open(gzip_db_location, 'rt') as db_as_zipfile:
    testcount = 0
    for seqio_record in SeqIO.parse(db_as_zipfile, "fasta"):
        if testcount < 10:
            print(seqio_record.id)
        
        
