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

for i in range(len(calls)):
	if(calls[i][1] in dictt.keys()):
		dictt[calls[i][1]]+=1
	else:
		dictt[calls[i][1]]=1

final_li = []
for i in range(len(calls)):
	if(calls[i][0] not in dictt.keys()):
		final_li.append(calls[i][0])

li = sorted(list(set(final_li)))

print("These numbers could be telemarketers: ")
for v in li:
	print(v)



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

