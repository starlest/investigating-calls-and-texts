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
tel_num_total_call_time = {}

def register_call_time(tel_number, call_time):
    if tel_number in tel_num_total_call_time:
        tel_num_total_call_time[tel_number] += call_time
    else:
        tel_num_total_call_time[tel_number] = call_time

for call in calls:
    calling_number = call[0]
    answering_number = call[1]
    call_time = int(call[3])
    register_call_time(calling_number, call_time)
    register_call_time(answering_number, call_time)

highest_tel_num = ""
highest_call_time = 0

for tel_num, total_call_time in tel_num_total_call_time.items():
    if total_call_time > highest_call_time:
        highest_tel_num = tel_num
        highest_call_time = total_call_time

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(highest_tel_num, highest_call_time))
