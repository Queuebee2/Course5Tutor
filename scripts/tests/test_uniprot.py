
from bioservices import UniProt

uniprot_handle = UniProt(verbose=False)


search = uniprot_handle.search("Z9JIV0", columns = "go(cellular component), subcellular locations, go(biological process), go(molecular function),feature(TRANSMEMBRANE), id, entry name, protein names, 3d")

print (search.split("\n")[1].split("\t"))


search = uniprot_handle.search("Z9JIV0", columns = "go(cellular component), subcellular locations, go(biological process), go(molecular function),feature(TRANSMEMBRANE), id, entry name, protein names, 3d")

print (search.split("\n")[1].split("\t"))
search = uniprot_handle.search("Z9JIV0", columns = "go(cellular component), subcellular locations, go(biological process), go(molecular function),feature(TRANSMEMBRANE), id, entry name, protein names, 3d")

print (search.split("\n")[1].split("\t"))
