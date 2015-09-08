#Q1

import csv
import collections

faculty = csv.reader(open("faculty.csv", "rb"))

degree=[]

for data in faculty:
    degree.append(data[1])
    
del degree[0]

degree = [d.replace('.', '') for d in degree]
degree = [d.lstrip() for d in degree]
degree = [d.split() for d in degree]

degreelist = []
for sublist in degree:
    for i in sublist:              
        if i in sublist:
            degreelist.append(i)

count=collections.Counter(degreelist)

print 'There are ' + str(len(count)) + ' different degrees.'
print count


#Q2

import csv
import collections

faculty = csv.reader(open("faculty.csv", "rb"))

titles=[]

for data in faculty:
    titles.append(data[2])
    
del titles[0]

count=collections.Counter(titles)

for t in range(len(titles)):
    tt = titles[t]
    titles[t] = tt[:-17] 
    
count=collections.Counter(titles)

print "There are " + str(len(count)) + " different titles."
print count


#Q3

import csv

faculty = csv.reader(open("faculty.csv", "rb"))

email=[]

for data in faculty:
    email.append(data[3])
    
del email[0]

for e in email:
    print e


#Q4

import csv
import re

faculty = csv.reader(open("faculty.csv", "rb"))

email=[]

for data in faculty:
    email.append(data[3])
    
del email[0]

ud=[] 
for i in email:
    domain = re.findall('@[\w.]+', i)
    
    for d in domain:
       if d not in ud:
           ud.append(d)
           
print 'There are ' + str(len(ud)) + ' different domains.'
print ud
