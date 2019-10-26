import gzip
from Bio import SeqIO
#TODO add todo to every file to add their imports to a list of
# depenencies


# bighelp from https://stackoverflow.com/questions/42757283/seqio-parse-on-a-fasta-gz


gzip_db_location = "/home/queue/SwissProt/uniprot_trembl.fasta.gz"

# gzip doc on modes https://docs.python.org/3/library/functions.html#open
# "rt" means "read text"? i think?


def printminmax():
    """ print the minimal and maximal size of seqio.ids """
    mi, ma = 25, 0
    with gzip.open(gzip_db_location, 'rt') as db_as_zipfile:
        testcount = 0
        for i, seqio_record in enumerate( SeqIO.parse(db_as_zipfile, "fasta")):

            if testcount < 10:
                print(print(seqio_record.seq))
            if len(seqio_record.id) < mi:
                mi = len(seqio_record.id)
            if len(seqio_record) > ma:
                ma = len(seqio_record.id)

            if i % 1000000 == 0:
                print(i)

    print(mi, ma)

# Doesnt work: cant take a filehandle, cant take a .gz
# only BGZF (blocked gzip format)
def test_get_raw():
    """ test and show the output of a get_raw method call on
        a (hopefully) valid SeqIO object
        oh and also test SeqIO.index"""
    #with gzip.open(gzip_db_location, 'rt') as db_as_zipfile:
    record_dict = SeqIO.index("uniprot_sprot.fasta.gz", "fasta")
    print(len(record_dict))
    for k, v in record_dict.items():
        print(k,v)
        break

    print('done get_raw')



with gzip.open(gzip_db_location, 'rt') as db_as_zipfile:

    linecount = 0
    for line in db_as_zipfile:
        linecount +=1

    print(linecount)












        
                

                    
