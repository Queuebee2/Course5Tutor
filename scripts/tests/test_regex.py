

lines = ["aabbcccccccc",     
         "ABCCCCCCABCCCCCC",
         "aaCbbCasdasd",
         "asdasdasudasdCdsCasd",
         "asCasdCasCASDasdsad",
         "CxC,asdasdasdsad",
         "CsaC",
         "abCxxCd",
         "ASDASDADjkwqjwejffae"]

import re


TARGET_PATTERN = re.compile('.[C]..[C].')




class TooManyError(Exception):
    def __init__(self, message="Too many. That was unexpected!"):
        super().__init__(message)
        
def find_target_pattern(string):
    """ Uses a regex object to find all occurences of
        a pattern within a string.

        The purpose (at this moment) is to only
        return values when only one unique match is found.

        An error will be raised when more than 1 match is found

    """

    # set TARGET_PATTERN as global re.compile('regexstring')
    matches = TARGET_PATTERN.findall(string)

    
    if matches:
        match_amt = len(matches)
        if match_amt > 1:
            raise TooManyError
        elif match_amt == 1:
            match = matches[0]
            return match
    else:
        return None

for line in lines:

    try:
        match = find_target_pattern(line)
        if match:
            index = line.index(match)
            seqLen = len(line)
            print('match of ', match, 'at', index ,"/", seqLen)
        else:
            index = -1      #implies there is no match
    except Exception as e:
        print('exception handled')








        
