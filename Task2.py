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
unique = {}

for record in calls:
    for num in record[:2]:
        if num not in unique:
            unique[num] = int(record[3])
        else:
            unique[num] += int(record[3])

key_max = max(unique.keys(), key=(lambda k: unique[k]))

print('{num} spent the longest time, {time} seconds, on the phone during September 2016.'.format(num = key_max, time = str(unique[key_max])))


