
from matplotlib import pyplot as plotter

original_names = open("original_names.txt", 'a')

""" helper functions """

def printDict(d):
    for k, v in d.items():
        print(k,":",v)
        
def scanFileFor(filepath, term):
    count = 0
    with open(filepath, 'r'):
        for line in file:
            if term in line:
                count+=1
    return count

def add():
    # placeholder to add a value in a textfile at a certain line
    pass



""" Main """


interestingTerms = {"PE=3":0, "PE=1":0,
                    "PE=2":0, "PE=4":0, "PE=5":0}

OSes = dict()


# counter to use to interrupt the loop if you just want to browse through
# uncomment the commented section in the file loop.
dontDoTooMuch = 0

with open("uniprot_thioredoxin_reviewed.fasta", 'r') as f:
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

            

def graphDict(d):
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
  
    # Aspect ratio - equal means pie is a circle

    axesObject.axis('equal')
    

    
    plotter.show()


printDict(interestingTerms)
graphDict(interestingTerms)
printDict(OSes)
graphDict(OSes)

