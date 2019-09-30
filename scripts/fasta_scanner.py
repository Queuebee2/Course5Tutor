# purpose: to analyse simple textfiles and create quick graphs, for now.
#
#
#

#imports
from matplotlib import pyplot as plotter
import os

# lets be nice to all OS users (this might hurt in the near upcoming future)
path_delim = os.sep

# directory paths (relative to script if ran as main)
OUT_DIR = "out_data"
IN_DIR = "in_data"

# set file here, todo: adapt to run through multiple files.
IN_FILE = IN_DIR+path_delim+"uniprot_thioredoxin_reviewed.fasta"


""" helper functions """

def printDict(d):
    # print keys and values from a dict next to eachother 
    for k, v in d.items():
        print(k,":",v)
        
def scanFileFor(filepath, term):
    # count occurences of a term (keyword) in a textfile
    count = 0
    with open(filepath, 'r'):
        for line in file:
            if term in line:
                count+=1
    return count

def addSomeValueToSomeTextfileAtSomePlace(textfile, val, place):
    # placeholder to add a value in a textfile at a certain line
    #idk
    pass


interestingTerms = {"PE=3":0, "PE=1":0,
                    "PE=2":0, "PE=4":0, "PE=5":0}

OSes = dict()


def pieGraphDict(d):
    # graphs the values in a dictionary with their key as label
    # doesn't work with nested dicts.
    
    values = []
    labels = []
    for k, v in d.items():
        values.append(v)
        labels.append(k + ": "+str(v))

    figureObject, axesObject = plotter.subplots()

    # Draw the pie chart
    axesObject.pie(values,
            labels=labels,
            autopct='%1.2f',
            startangle=90)

    axesObject.axis('equal')
    plotter.show()

def main():
    # counter to use to interrupt the loop if you just want to browse through
    # uncomment the commented section in the file loop.
    dontDoTooMuch = 0


    # set global IN_FILE at top of script pls
    with open(IN_FILE, 'r') as f:
        PEs = 0 
        for l in f:
            line = l.strip()
            
                    
            if line.startswith(">"):
                #print(line)
                dontDoTooMuch+= 1

                for part in line.split(" "):
                    if part.startswith("OS"):
                        thing = part.split("OS=")[1]
                        if thing in OSes:
                            OSes[thing] +=1
                        else:
                            OSes[thing] = 1
                
                for term in interestingTerms:
                    if term in line:
                        interestingTerms[term]+=1

                #if dontDoTooMuch % 25 == 0:
                #    b = input("press enter do 25 more")
                #    if b in 'nostopb' and b != "":
                #        break

                
        
    printDict(interestingTerms)
    pieGraphDict(interestingTerms)
    printDict(OSes)
    pieGraphDict(OSes)


main()

