import pygal
import sys
LINE_ONE_ELEMS= 17

f = open("midterm2020.txt", "r")
data= f.read().split()

# get longest user 0 wait time, and total values for user0
user0valCount= 0
longestWait= 0
temp= 0
elems= len(data)
counter= LINE_ONE_ELEMS
while(counter < elems):
    temp= int(data[counter])
    if(temp > longestWait):
        longestWait= int(data[counter])
    counter+=5
    user0valCount+= 1

# initialise wait times frequency array
timesWaitedFreq = []
for i in range(longestWait+1):
    timesWaitedFreq.append(0)

# populate wait times frequency array
counter= LINE_ONE_ELEMS
while(counter < elems):
    temp= int(data[counter])
    timesWaitedFreq[temp]+= 1
    counter+=5

# convert freqs to probabilities
counter= 0
while(counter < longestWait + 1):
    timesWaitedFreq[counter]= timesWaitedFreq[counter] / user0valCount
    counter+= 1

# load bar set for histo
histoBarSet = [(0,0,0)] * (longestWait + 1)
for i in range(longestWait + 1):
    histoBarSet[i]= (timesWaitedFreq[i], i, i+1)

# make histo
pmf = pygal.Histogram(title=u'PMF | x-axis: time taken (ms), y-axis: probability (%)')
for i in range(longestWait+1):
    print(i,"= ",timesWaitedFreq[i])
pmf.add('', histoBarSet)
pmf.render_to_file('q1.svg')