import pygal
import sys
from random import randint
from sort import sort
import statistics
LINE_ONE_ELEMS= 17
MAKE_PERCENT= 100
BOOTSTRAP_SAMPLE_SIZE= 20
BOOTSTRAP_AMOUNT_SAMPLES= 50 # return this to 10,000
CONFIDNC_INTRVL_1= 15
CONFIDNC_INTRVL_2= 95
A_LARGE_NUMBER= 99999999

f = open("midterm2020.txt", "r")
data= f.read().split()

################################### (1) i) ###################################
# extract user 0 data from data
user0data= []
i= LINE_ONE_ELEMS
elems= len(data)
while(i < elems):
    user0data.append(int(data[i]))
    i+= 5

# get longest user 0 wait time
temp= 0
longestWait= 0
for i in range(len(user0data)):
    temp= user0data[i]
    if(temp > longestWait):
        longestWait= user0data[i]

# initialise wait times frequency array, and prob of time array
timesWaitedFreq= []
probOfTime= []
for i in range(longestWait + 1):
    timesWaitedFreq.append(0)
    probOfTime.append(0)

# populate wait times frequency array
i= LINE_ONE_ELEMS
for val in user0data:
    timesWaitedFreq[val]+= 1

# calculate probabilities from freqs
for i in range(longestWait + 1):
    probOfTime[i]= (timesWaitedFreq[i] / len(user0data)) * MAKE_PERCENT

# load bar set for histo
histoBarSet= [(0,0,0)] * (len(user0data))
for i in range(len(probOfTime)):
    histoBarSet[i]= (probOfTime[i], i, i+1)
    # print("height: ",probOfTime[i],". x(",i,",",i+1,").")

# make histo
pmf= pygal.Histogram(title=u'PMF | x-axis: time taken (ms), y-axis: probability (%)')
pmf.add('', histoBarSet)
pmf.render_to_file('q1.svg')

################################### (1) ii) ###################################

ones= 0
allConnections= 0
for i in range(len(timesWaitedFreq)):
    if(i <= 10):
        ones+= timesWaitedFreq[i]
    allConnections+= timesWaitedFreq[i]
probOfOne= (ones / allConnections) * MAKE_PERCENT
print("Probability(X = 1): ", probOfOne)

################################### (1) iii) ###################################
# BOOTSTRAPPING
def getValsInIntrvl(vals, medianPos, intrvl):
    valsIn= [vals[medianPos]]
    i= medianPos # i is left pointer array offset
    j= medianPos # j is right pointer array offset
    intrvlSize= round((len(vals) / 100) * intrvl) - 1
    while(len(valsIn) < intrvlSize):
        if(i > 0):
            leftValCost= vals[i] - vals[i - 1]
        else:
            leftValCost= A_LARGE_NUMBER
        if(j < (len(vals) - 1)):
            rightValCost= vals[j + 1] - vals[j]
        else:
            rightValCost= A_LARGE_NUMBER
        if(leftValCost > rightValCost): # expand span to the right
            j+= 1
            valsIn.append(vals[j])
        else: # expand span to the left
            i-= 1
            valsIn.append(vals[i])
    return valsIn

sampleMeans= []
for i in range(BOOTSTRAP_AMOUNT_SAMPLES):
    sampleSum= 0
    for j in range(BOOTSTRAP_SAMPLE_SIZE):
        random= randint(0, len(user0data) - 1)
        sampleSum+= user0data[random]
        # print(random)
    sampleMeans.append(sampleSum / BOOTSTRAP_SAMPLE_SIZE)
sampleMeans= sort(sampleMeans)
'''for i in range(len(sampleMeans)):
    print(sampleMeans[i])'''
medianOfMeans= statistics.median(sampleMeans)
i= 0
while(medianOfMeans > sampleMeans[i]):
    i+= 1
# print("medianOfMeans: ",medianOfMeans)
nintyFiveIntrvl= getValsInIntrvl(sampleMeans, i, CONFIDNC_INTRVL_2)
# print("------------------------------")
for val in nintyFiveIntrvl:
    print(val)
fifteenIntrvl= getValsInIntrvl(sampleMeans, i, CONFIDNC_INTRVL_1)
'''print("------------------------------")
for val in fifteenIntrvl:
    print(val)'''

# 

