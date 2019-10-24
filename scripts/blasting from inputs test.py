from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

from Bio import SearchIO
from Bio import SeqIO
from Bio import Entrez

from bioservices import UniProt

Entrez.email = "MJ.Lambers@student.han.nl" # ALWAYS TELL THEM WHO YOU ARE

def first():

    fasta = open("testfasta.txt", 'r').read()
    blast_out = open("blast_results_fasta.fa", 'w')

    with NCBIWWW.qblast("blastp", "nr", fasta) as result_handle:
        with open("blast_xmltest.xml", 'w') as xml_file:
            xml_file.write(result_handle.read())

            # parse xml and write to fasta
            blast_qresult = SearchIO.read("blast_xmltest.xml", 'blast-xml')
            records = []
            for hit in blast_qresult:
                print(dir(hit))
                records.append(hit[0].hit)
                print(hit[0].hit)
            SeqIO.write(records, blast_out, "fasta")
            

def second():
    # parse xml and write to fasta
    blast_qresult = SearchIO.read("blast_xmltest.xml", 'blast-xml')
    records = []
    for hit in blast_qresult:
        print(hit[0].hit)
        records.append(hit[0].hit)
        
        if 'SP' in hit[0].hit.id:
            print ("ID:",hit[0].hit.id)

    # god what a mess I've made
    print(hit.accession)
    print(dir(hit[0].hit))
    print(type(hit[0].hit))
    print("SEQUENCE:",hit[0].hit.seq)
    print(str(hit[0].hit.seq))
    f = open('entreztext.fasta', 'a')
    f.write(handle.read())
    handle.close()
    f.close()
    
#second()

class InvalidIdError(Exception):
    """When using an identifier yield unexpected results"""
    def __init__(self, message="That ID can't be found or doesn't exist"):
        super().__init__(message)

class TooManyError(Exception):
    """When there's too much of something"""
    def __init__(self, message="Too many. That was unexpected!"):
        super().__init__(message)

class UrgentUnknownError(Exception):
    """When I dont know what in fruits name happened"""
    def __init__(self, message):
        message = "CALL HELP IMMEDIATELY " + message
        super().__init__(message)

def test1():

    u = UniProt()


    # working bob
    bob = fetch_fasta_from_uniprot(u, 'P29317', True)
    print(bob)

    # toomanyError bob
    try:
        bob = fetch_fasta_from_uniprot(u, ['P29317','P13929'], True)
        print(bob)
    except TooManyError:
        # expected outcome
        print('toomanyerror handled')

    # toomanyError bob
    try:
        bob = fetch_fasta_from_uniprot(u, 'P29317'+',\P13929', True)
        print(bob)
    except InvalidIdError:
        # expected outcome
        print('InvalidIdError 400 handled')

        # 
        
    # InvalidIdError bob
    try:
        bob = fetch_fasta_from_uniprot(u, "IwantA404CodePlease", True)
        print(bob)
    except InvalidIdError:
        # expected outcome
        print('InvalidIdError 404 handled')
        

def third(verbose=True):
    """ how to iterate over a blast result?"""
    blast_file = open("blast_xmltest.xml", 'r')
    blast_records = NCBIXML.parse(blast_file)

    for blast_record in blast_records:
        if verbose: print("using record:",blast_record,"\nfrom records:",blast_records)
        for alignment in blast_record.alignments:
            if verbose: print("using alignment:", alignment, "\nfrom alignments:",blast_record.alignments)
            for hsp in alignment.hsps:
                if verbose:
                    print('****Alignment****')
                    print('sequence:', alignment.title)
                    
        
third()
