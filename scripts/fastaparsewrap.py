


def make_header_spit_out_a_database(header):
    if header.startswith(">"):
        header = header[1:]

    stuff = header.split("|")
    datbase_column
def fasta_burrito(file_handle):
    file = file_handle
    # Assume fasta starts with >
    header = file.readline()
    # check if that assumption was true.
    assert header.startswith(">"), "file not properly Fasta Formatted"

    sequence = ''
    # wrap this
    for l in file:
        line = l.strip("\n")
        if line.startswith(">"):
            if header != '':
                
                pass
# TODO                  detect which database it comes from?        https://en.wikipedia.org/wiki/FASTA_format#NCBI_identifiers    
                # SWISS-PROT 	    sp|accession|name       ''
                # PDB 	            pdb|entry|chain         ''
                # Refseq protein    >NP_id                  https://www.ncbi.nlm.nih.gov/books/NBK50679/
                

                # check if it already exists in our database (?? will this be costly?)

                # Do we care about redundant sequences?
                # Proposal: remove junction table and add 3 db-id columns to
                # primary database table 
                # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5225397/
                # http://weizhongli-lab.org/cd-hit/


            # prep loop for next sequence
            yield ("TEST " + header), sequence
            header = line
            sequence = ''

        else:
            sequence += line

        

# find GO terms and other traits for each protein here or in loop?

            
with open('testfasta.txt', 'r') as file:
    for header, sequence in fasta_burrito(file):
        print(header)
        
