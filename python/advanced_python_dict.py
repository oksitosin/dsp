#Q6

import csv
import collections
from itertools import islice

faculty = csv.reader(open("faculty.csv", "rb"))

degree=[]
titles=[]
lastn=[]
email=[]

for data in faculty:
    degree.append(data[1])
    titles.append(data[2])
    lastn.append(data[0])    
    email.append(data[3])
    
del degree[0]
del titles[0]
del lastn[0]
del email[0]

degree = [d.replace('.', '') for d in degree]
degree = [d.lstrip() for d in degree]

            
for t in range(len(titles)):
    tt = titles[t]
    titles[t] = tt[:-17] 
    
lastn = [l.split()[-1] for l in lastn]    
lastn=tuple(lastn)        

val=zip(lastn,degree,titles,email)

faculty_dict = dict()

for line in val:
    if line[0] in faculty_dict:
        faculty_dict[line[0]].append(line[1:])
    else:
        faculty_dict[line[0]] = [line[1:]]

x = itertools.islice(faculty_dict.items(), 0, 3)

for key, value in x:
    print key, value
    
    
#Q7

import csv
import collections
from itertools import islice

faculty = csv.reader(open("faculty.csv", "rb"))

degree=[]
titles=[]
lastn=[]
email=[]
firstn=[]

for data in faculty:
    degree.append(data[1])
    titles.append(data[2])
    lastn.append(data[0])    
    email.append(data[3])
    firstn.append(data[0])
    
del degree[0]
del titles[0]
del lastn[0]
del email[0]
del firstn[0]

degree = [d.replace('.', '') for d in degree]
degree = [d.lstrip() for d in degree]

            
for t in range(len(titles)):
    tt = titles[t]
    titles[t] = tt[:-17] 
    
lastn = [l.split()[-1] for l in lastn]    
lastn=tuple(lastn)  

firstn = [f.split()[0] for f in firstn]
firstn = [f.lstrip() for f in firstn]
firstn = tuple(firstn)      

val=zip(firstn,lastn,degree,titles,email)

professor_dict = dict()

for line in val:
    if line[0:2] in professor_dict:
        professor_dict[line[0:2]].append(line[2:])
    else:
        professor_dict[line[0:2]] = [line[2:]]

x = itertools.islice(professor_dict.items(), 0, 3)

for key, value in x:
    print key, value
    
#Q8
#In addition to Q7 code, the following will sort the dictionary by last name.

pds = sorted(professor_dict.items(), key=lambda l: l[0][1])[:3]
print pds
