import os

# lets be nice to all OS users (this might hurt in the near upcoming future)
path_delim = os.sep


#
# SET FILE HERE
#

IN_DIR = "in_data"
IN_FILE = IN_DIR+path_delim+"hmmer_hmm_1.hmm"

###############################################################################

allLetters = 'QWERTYUIOPASDFGHJKLZXCVBNMmnbvcxzlkjhgfdsapoiuytrewq'

markovWord = ''

didHeaders = False

def testHeaders(l):
    # when we find all these chars in a line, the matrix starts
    for char in "ACDEFGHIKLMNPQRSTVWY":
        if char not in l:
            return False
    return True


with open(IN_FILE, 'r') as f:
    for line in f:
        if not didHeaders:
            didHeaders = testHeaders(line)
        else:
            try:
                # the end of some lines look like      nnn x - - -
                # with nn being numbers and x being a letter for a protein
                # - being literally dashes, not sure what other possibilities
                # are, yet.
                # by splitting the whole line and taking the [-4]th element
                # the character we obtain seems to be part of the consensus
                # pattern
                w = line.split()[-4]
                if len(w) == 1 and w in allLetters:
                    markovWord += w
            except:
                # 
                pass


# consensus??
print(markovWord)
