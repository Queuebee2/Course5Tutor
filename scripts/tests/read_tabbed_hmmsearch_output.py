from Bio import SearchIO


usedcmd ="""hmmsearch --tblout myhits.tbl --acc --noali hmm_file.hmm /home/queue/SwissProt/uniprot_sprot.fasta.gz                                                                                           

"""
result = next(SearchIO.parse('myhits.tbl', 'hmmer3-tab'))


c = 0

for hit in result.hits:


    if c < 10:
        print("ID:",hit.id)
        print("ACESS:",hit.acession)
        print("EVAL:",hit.evalue) 

    else:
        print(hit.id)
        print(dir(hit))
        break
        
    c+=1
