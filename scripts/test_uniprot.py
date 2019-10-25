
from bioservices import UniProt

uniprot_handle = UniProt(verbose=False)

# default columns to select in uniprot search
DEFAULT_SELECTION = ["go(biological process)","go(cellular component)",
                     "go(molecular function)"]


def get_uniprot_stuff(uniprot_handle, acession, columns_list=DEFAULT_SELECTION,
                      verbose=False):
    """ """
    
    result = uniprot_handle.search(acession, columns=",".join(columns_list))

    column_value_dict = dict()

    for i, column in enumerate(columns_list):
            try:
                value = result.split("\n")[1].split("\t")[i]
            except IndexError:
                value = None
                
            if verbose: print(column, value)
            
            column_value_dict[column] = value
        
    return column_value_dict


d = get_uniprot_stuff(uniprot_handle, "Z9JIV0", verbose=True)
print(d)
