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
