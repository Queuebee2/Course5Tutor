from Bio import SearchIO


usedcmd ="""hmmsearch --tblout myhits.tbl --acc --noali hmm_file.hmm /home/queue/SwissProt/uniprot_sprot.fasta.gz                                                                                           

"""
tabs = SearchIO.parse('myhits.tbl', 'hmmer3-tab')


c = 0
for result in tabs:

    if c < 2:

        print(result)
        print(dir(result))
        

    else:
        break

    c+=1
