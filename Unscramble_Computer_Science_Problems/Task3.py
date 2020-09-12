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

bang = {}
for val in calls:
	if(val[0][0:5]=='(080)'):
		bang[val[0]]=val[1]

final_li = []
for k,v in bang.items():
	if(' ' in v and v[0] in ['7','8','9']):
		final_li.append(v[0:4])
	elif(' ' not in v and v[0:3]=='140'):
		final_li.append(v[0:3])
	elif(v[0]=='(' and v[1]=='0'):
		final_li.append(v[1:v.find(")")])
		
li = sorted(list(set(final_li)))
print('The numbers called by people in Bangalore have codes:')
for v in li:
	print(v)

tot_c=0
c=0
for i in range(len(calls)):
	if(calls[i][0][0:5]=='(080)'):
		tot_c+=1
	if(calls[i][0][0:5]=='(080)' and calls[i][1][0:5]=='(080)'):
		c+=1

val = (c/tot_c) * 100
print(str(round(val,2))+' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
