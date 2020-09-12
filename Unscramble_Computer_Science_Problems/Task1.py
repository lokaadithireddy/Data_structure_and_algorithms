"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

dictt = {}
for i in range(2):
	for j in range(len(texts)):
		if(texts[j][i] in dictt.keys()):
			dictt[texts[j][i]]+=1
		else:
			dictt[texts[j][i]]=1

for i in range(2):
	for j in range(len(calls)):
		if(calls[j][i] in dictt.keys()):
			dictt[calls[j][i]]+=1
		else:
			dictt[calls[j][i]]=1

print('There are '+str(len(dictt))+' different telephone numbers in the records.')



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
