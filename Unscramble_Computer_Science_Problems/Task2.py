"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dictt = {}
for i in range(2):
	for j in range(len(calls)):
		if(calls[j][i] in dictt):
			dictt[calls[j][i]]+=int(calls[j][3])
		else:
			dictt[calls[j][i]]=int(calls[j][3])
maxim = -1
for k,v in dictt.items():
	if(v>maxim):
		maxim=v
		tele=k

print(str(tele)+' spent the longest time,'+ str(maxim)+' seconds, on the phone during September 2016.')


























