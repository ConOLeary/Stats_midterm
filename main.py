import pygal
import sys
LINE_ONE_ELEMS= 17
MAKE_PERCENT= 100
BOOTSTRAP_SAMPLE = 50

f = open("midterm2020.txt", "r")
data= f.read().split()

################################### (1) i) ###################################
# get longest user 0 wait time, and total values for user0
user0valCount= 0
longestWait= 0
temp= 0
elems= len(data)
i= LINE_ONE_ELEMS
while(i < elems):
    temp= int(data[i])
    if(temp > longestWait):
        longestWait= int(data[i])
    i+=5
    user0valCount+= 1

# initialise wait times frequency array, and prob of time array
timesWaitedFreq= []
probOfTime= []
for i in range(longestWait + 1):
    timesWaitedFreq.append(0)
    probOfTime.append(0)

# populate wait times frequency array
i= LINE_ONE_ELEMS
while(i < elems):
    temp= int(data[i])
    timesWaitedFreq[temp]+= 1
    i+=5

# calculate probabilities from freqs
i= 0
while(i < longestWait + 1):
    probOfTime[i]= (timesWaitedFreq[i] / user0valCount) * MAKE_PERCENT
    i+= 1

# load bar set for histo
histoBarSet= [(0,0,0)] * (longestWait + 1)
for i in range(longestWait + 1):
    histoBarSet[i]= (probOfTime[i], i, i+1)

# make histo
pmf= pygal.Histogram(title=u'PMF | x-axis: time taken (ms), y-axis: probability (%)')
pmf.add('', histoBarSet)
pmf.render_to_file('q1.svg')

################################### (1) ii) ###################################
zeros= 0
ones= 0
for i in range(longestWait + 1):
    if(timesWaitedFreq[i] > 10):
        ones+= 1
    else:
        zeros+= 1
probOfOne= (ones / zeros) * MAKE_PERCENT
print("Probability(X = 1): ", probOfOne)

################################### (1) iii) ###################################
