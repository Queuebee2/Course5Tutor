from sys import argv
import subprocess
import os
import os.path

import re
import gzip
from time import sleep
import traceback

from Bio import SearchIO
from bioservices import UniProt
from DbConnector import DbConnector

#important globals

# regex object used in find_target_pattern(string):
TARGET_PATTERN = re.compile('[C]..[C]')

# entry-point filenames
FASTA_DATABASE = '/home/queue/SwissProt/uniprot_sprot.fasta.gz'#must be zip.gz!
MAIN_FASTA_FILENAME = 'in_data/uniprot_seqs_rev.fasta.fasta'
FASTA_TOADD_FILENAME = 'this_iteration_fastas_to_add.fasta'

# temp filename
MSA_FILENAME = 'msa.msa'
HMM_FILENAME = 'hmm.hmm'
HMM_SEARCH_TAB_OUTPUT_FILENAME = 'hmmsearch3_tab_output.tbl'
BLAST_OUTPUT = 'blast_output.xml'
LOG_FILENAME = 'logfile.log'


# columns used in fetching data from uniprot
DEFAULT_SELECTION = ["go(biological process)","go(cellular component)",
                     "go(molecular function)"]

# searchoptions for hmmsearch
HMMSEARCH_OPTIONS = " --tblout " + HMM_SEARCH_TAB_OUTPUT_FILENAME + \
                    " --acc --noali "

# custom errors
class TooManyError(Exception):
    """When there's too much of something"""
    def __init__(self, message="Too many. That was unexpected!"):
        super().__init__(message)

class InvalidIdError(Exception):
    """When using an identifier yield unexpected results"""
    def __init__(self, message="That ID can't be found or doesn't exist"):
        super().__init__(message)

class UrgentUnknownError(Exception):
    """When I dont know what in fruits name happened"""
    def __init__(self, message):
        message = "CALL HELP IMMEDIATELY " + message
        super().__init__(message)



# helper functions
def find_target_pattern(string ,verbose = True):
    """ Uses a regex object to find all occurences of
        a pattern within a string.

        The purpose (at this moment) is to only
        return values when only one unique match is found.

        An error will be raised when more than 1 match is found
    """
    #TODO SET VERBOSE OFF AGAIN
    # set TARGET_PATTERN as global re.compile('regexstring')
    if verbose: print("finding matches")
    matches = TARGET_PATTERN.findall(string)
   
    if matches:
        match_amt = len(matches)
        if match_amt > 1:
            if verbose: print("TooManyError: too many patterns error")
            raise TooManyError
        elif match_amt == 1:
            match = matches[0]
            if verbose: print("found",match)
            return match
    else:
        if verbose: print("there aren't any matches!")
        return None

    print(20*"something funny happened")
        
def create_msa_mafft(MAIN_FASTA_FILENAME=MAIN_FASTA_FILENAME,
                     msa_destination_filename=MSA_FILENAME, verbose=False):
    """calls 'mafft' through the shell to create a
       multiple sequence alignment (msa_filename)

    ARGS:
        MAIN_FASTA_FILENAME: string
            relative path (just a filename) of a file containing fasta
            sequences to be aligned

        msa_destination_filename: string
            relative path in which to save the multiple sequence alignment

    """

    # Check whether msa has already been made
    if os.path.isfile(msa_destination_filename):
        print("msa already exists, overwriting!")
    # Execute command if msa hasn't been made before

    cmd = "mafft " + MAIN_FASTA_FILENAME + " > " + msa_destination_filename
    e = subprocess.check_call(cmd, shell=True)
    if verbose:  print(e)
    return

def create_hmm(msa_filename=MSA_FILENAME,
               hmm_destination_filename=HMM_FILENAME, verbose=False):
    """calls 'hmmbuild' through the shell to create a hmm profile
       from a multiple sequence alignment (msa_filename)

    ARGS:
        msa_filename: string
            relative path (just a filename) of
            a file containing a valid MSA

        hmm_destination_filename: string
            relative path in which to create
            a hmm profile using hmmer

    """

    # Check whether hmm has already been made
    if os.path.isfile(hmm_destination_filename):
        print("hmm already exists, overwriting!")
    # Execute command if hmm hasn't been made before

    cmd = "hmmbuild " + hmm_destination_filename + " " + msa_filename
    e = subprocess.check_call(cmd, shell=True)
    if verbose:  print(e)
    return

def do_hmm_search(hmm_filename=HMM_FILENAME,
                  fasta_database=FASTA_DATABASE,
                  options= HMMSEARCH_OPTIONS ,
                  verbose=False):
    """calls 'hmmsearch' through the shell to ty and
       create a  TODO <whatever the format is>
       by performing a hmmsearch on a database file

    ARGS:
        hmm_filename: string
            relative path (just a filename) of
            a file containing a valid profile HMM

        fasta_database: string
            relative path to a (fasta) database file
            examples @ https://www.uniprot.org/downloads

    """

    # Check whether hmm has already been made
    if os.path.isfile(HMM_SEARCH_TAB_OUTPUT_FILENAME):
        print("hmmsearchfile already exists, but i dont care")
    # Execute command if hmm hasn't been made before
    else:
        cmd = "hmmsearch {} {} {}".format(options,hmm_filename,fasta_database)
        print('hmmsearching:',cmd)
        e = subprocess.check_call(cmd, shell=True)
        if verbose:  print(e)
    return


def fetch_fasta_from_local_zip_db(accession, local_zip_db_name=FASTA_DATABASE,
                                  verbose=True):
    """ hacky function to gather header + sequence by accession in a
        downloaded database file (zipped fasta)

    """
    if verbose: print('trying to open gzip and find',accession)
    with gzip.open(gzip_db_location, 'rt') as db_as_zipfile:
        if verbose: print("welcome to excessive verbosityPrints ltd© ")
        header = ''
        seq = ''
        lines = 0
        for line in db_as_zipfile:

            if lines % 250000 == 0:
                print('looked through', lines,'lines for',accession)
            if line.startswith(">") and header != '':
                print(header, "\n",seq)
                if seq != '':
                    if verbose: print("returning fetch!",header[:6],seq[:6])
                    return header, seq
                else:
                    if verbose: print("fetchfromzIp EXCEPTION!!!!")
                    # TODO MAKE CUSTOM EXCEPTION
                    raise Exception("seq not filled in"+\
                        "fetch_fasta_from_local_zip_db!")
            
            if accession in line:
                if verbose: print("stripping a header from its trailingnewl")
                header = line.strip("\n")

            if header != '' and not line.startswith(">"):
                if verbose: print("appending to seq!",len(seq))
                seq += line.strip("\n")

        # TODO MAKE CUSTOM EXCEPTION
        raise Exception("something weird happened in"+\
                        "fetch_fasta_from_local_zip_db")
                

# prolly not gonna use lol
def fetch_fasta_from_uniprot(uniprot_handle, accession, verbose=True):
    """should return the header+sequence of a swissprot entry in
       fasta format, but otherwise lets you know it didn't.

    arguments
    uniprot_handle: bioservices.Uniprot object to execute the fetch

    accession: str (preferrably), can be a list too. Let's keep it
              the way bioservices had it made. very convenient.

    returns: str containing a fasta file for max 1 entry

    throws: all kinds of errors. Wrong id error, too many
            (unexpected result) errors,
            400, 404 errors.
            UnknownError s.

    
    """
    print("looking for fasta for", accession)
    fasta_str = uniprot_handle.retrieve(accession, frmt='fasta')
    if verbose: print('got a fasta from', accession)
    if type(fasta_str) == str:
        # sometimes this dumb retrieve func returns just 1 string,
        # the fasta itself. This is the expected result
        header_seqlist = fasta_str.split("\n")
        header = header_seqlist[0]
        seq = header_seqlist[1]
        return header, seq
    
    elif type(fasta_str) == list:
        # but then, sometimes, like if you accidentally were to give it 2
        # accession identifiers, it would return a list of fasta strings.
        print('fetch_fasta returned too many fasta strings!')
        raise TooManyError('fetch_fasta returned too many fasta strings!')
    
    elif (fasta_str == '404') or (fasta_str == 404):
        # then if an id returns a 404 page, it just returns '404'
        # so that's really convenient, too, yes.
        print(str(accession) + " yields a 404 error!")
        raise InvalidIdError(str(accession) + " yields a 404 error!")
        

    elif (fasta_str == '400') or (fasta_str == 400):
        # oh apparently something can cause it to return a 400 error too
        print(str(accession) + " yields a 400 error!")
        raise InvalidIdError(str(accession) + " yields a 400 error!")
    else:
        # gosh darnit
        print('UrgentUnknownError:','type fasta_str:' + str(type(fasta_str)) +
                                 ' accession id:' + str(accession))
        raise UrgentUnknownError('type fasta_str:' + str(type(fasta_str)) +
                                 ' accession id:' + str(accession))



def get_uniprot_stuff(uniprot_handle, accession, columns_list=DEFAULT_SELECTION,
                      verbose=True):
    """ TODO DOCSTRING
        in goes a Uniprot object from bioservices along with a
        swissprot id and a list of expected columns

    """
    print('trying to find GOTERMS for',accession)

    foundGO = False
    while not foundGO:
        if verbose: print("looking up GO terms")
        result = uniprot_handle.search(accession, columns=",".join(columns_list))
        if result:
            foundGO = True
        sleep(10)

    column_value_dict = dict()
    
    for i, column in enumerate(columns_list):
        if verbose:
            print(i)
            print(column, result.split("\n")[1].split("\t")[i-1])   #TODO FIX THIS UGLY THING
            try:
                value = result.split("\n")[1].split("\t")[i]
            except IndexError:
                value = None              

            column_value_dict[column] = value
        
    return column_value_dict


def iterate_hmm_search_tab_results(filename=HMM_SEARCH_TAB_OUTPUT_FILENAME,
                                   verbose=False):
    """ GENERATOR!!!
        iterate over hmmsearch3 tab output using SearchIO.parse

    yields:
        Bio.< ? ? >.Hit.id
        Bio.< ? ? >.Hit.evalue

    """
    result = next(SearchIO.parse(filename, 'hmmer3-tab'))
    for hit in result.hits:
        yield hit.id, hit.evalue
    
    
def make_obscure_SQL_part(d):
    """ takes a dictionary and puts the value in the right order
        based on the order of keys in the database
        with quotes so it can be entered as a string/text in a sql insert"""
    keys_in_order = [k for k in DEFAULT_SELECTION]
    return "'" + "','".join([d[k] for k in keys_in_order]) + "'"
        

def merge_fasta(to_add, main_file):

    # todo

    # make temp file

    # iterate over to_add

    # check if any header:sequence exists in main_file

        # if not, add it to temp

        # else, skip

    # write whole main_file to temp and rename it
    # OR add all temp_file lines to main_file.
    
    pass


def in_fasta(accession,fastafile=MAIN_FASTA_FILENAME):
    with open(fastafile, 'r') as f:
        for line in f:
            if accession in f:
                return True
    return False

def add_to_temp(lines):
    with open(FASTA_TOADD_FILENAME, 'a') as out:
        out.write(lines + "\n")

def update_main_fasta():
    with open(MAIN_FASTA_FILENAME, 'a') as out:
        out.write("\n") # to be sure
        with open(FASTA_TOADD_FILENAME, 'r') as infile:
            header = ''
            seq =''
            for line in infile:
                if line.startswith(">"):
                    if header != '':
                        out.write(header)
                        out.write(seq)
                    header = line
                    seq = ''
                else:
                    seq += line

        out.write(header)
        out.write(seq)
    
def important_mainloop(verbose=1):
    # todo set verbose default to False again one day or another im gonna find ya im gonna getcha getcha getcha getcha

    # create an object to handle communications with mySQL database
    db = DbConnector() 
    

    # create uniprot handle object
    # todo: find out if 'handle' is the right terminology here
    uniprot_handle = UniProt(verbose=True)


    # determine input file(s)
        # check validity
        # combine multiple fasta's into one for msa

    
    # set main loop condition
    # this could be NOT running out of results or
    # having more than 50% of results be results we already
    # found
    running = True
    iteration = db.selecx_max_iteration()
    
    # 'running' loop
    while running:
        
        # msa
        
        create_msa_mafft()
        if verbose: print("main: trying to create msa...")

        # hmm
        create_hmm()
        if verbose: print("main: trying to create phmm...")

        # hmm search
        do_hmm_search()
        if verbose: print("main: trying to do hmmsearch...")


        # iterate hmm search results
        innerLoop = True
        loopcount = 0

        search_result_terator = iterate_hmm_search_tab_results()
        
        for identifier, evalue in search_result_terator:

            if verbose:
                if loopcount % 10 ==0:
                    print('fasta files:', loopcount)

            
            if verbose: print('id:',identifier, 'eval:',evalue)

            actual_id = identifier.split("|")[1]


            # sql select to check if it exists in our db
            if db.exists_protein(actual_id):
                if verbose: print('skipped', actual_id)
                continue  # skip (doesnt check if other values filled though)
            else:
                if verbose:print(actual_id,'not in db, looking for header..')
                
                header, seq = fetch_fasta_from_uniprot(uniprot_handle, actual_id)

    
                # fetch header LOCALLY, fasta from local database
                # NEVERMIND WE DEPRECATE THIS ONE SINCE ITS NOT WORKING
                # header, seq = fetch_fasta_from_local_zip_db(actual_id)

                
                if verbose: print(header[:22], seq[:20])

                # find pos_2c
                try:
                    pos_2c = find_target_pattern(seq)
                
                    if pos_2c:
                        pos_2c = seq.index(pos_2c)
                    else:
                        pos_2c = -1
                except TooManyError:
                    pos_2c = -200
                    
                if verbose: print('pos 2c:', pos_2c)

                

                foundGO=False
                while not foundGO:
                    if verbose: print("looking up GO terms")
                    try:
                        GO_STUFF_D = get_uniprot_stuff(uniprot_handle, actual_id)
                    except Exception as e:
                        print(e)
                        print("TODO FIGURE OUT HOW TO ENABLE ALL DEBUFGPRINTS$RITW")
                    if GO_STUFF_D:
                        
                        foundGO = True
                        
                    #print('zzzzz')
                    #sleep(10)
                    
                if verbose > 1:
                    for k, v in GO_STUFF_D.items():
                        print("GO:",k, v)
        
               # obscure_GO_stuff = make_obscure_SQL_part(GO_STUFF_D)

                
                query = f"""INSERT INTO PROTEIN VALUES(
                        NULL,
                        '{actual_id}',
                        '{header}',
                        '{seq}',
                        {iteration},
                        '{GO_STUFF_D['go(biological process)']}',
                        '{GO_STUFF_D['go(cellular component)']}',
                        '{GO_STUFF_D['go(molecular function)']}',
                        {pos_2c});
                        """
                
                db.commit_query(query)
                if verbose > 1 : print('queried ', query)

                if not in_fasta(actual_id) and not in_fasta(FASTA_TOADD_FILENAME, actual_id):
                    add_to_temp(header)
                    add_to_temp(seq)
                
        #outofinnerloop
        iteration += 1
        update_main_fasta()
        

                    
        
        
        # repeat?
    
def main():

    # exceptions 
    caughtMistakes = 0


    while caughtMistakes< 5:
        """ as long as there are no errorcounts over 5,
            retry this loop"""
        try:
            important_mainloop()

        # exceptions we know how to handle
        #
        # here.

        # uknown exceptions
        except Exception as SomeUnknownException:
            print("there was a horrible exception!")
            e = str(type(SomeUnknownException))
            print("Error str:",e)
            print("traceback:",traceback.format_exc())
            print("Unknown except:",SomeUnknownException)
            
            with open('logfile.log', 'a') as logfile:
                logfile.write(e+"\t"+traceback.format_exc()+"\n")
                

            if caughtMistakes > 5:
                print('too many exceptions caught')

            caughtMistakes +=1
            
   
        

    


if __name__ == "__main__":
    print('running from main')
    main()

