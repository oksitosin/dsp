import csv

faculty = csv.reader(open("faculty.csv", "rb"))

email=[]

for data in faculty:
    email.append(data[3])
    
del email[0]

c = csv.writer(open("emailcsv.csv", "wb"))

for e in email:
    c.writerow([e])
