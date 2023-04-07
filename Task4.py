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

possible_telemarketers = set()
calling_numbers = set()
receiving_numbers = set()
text_sender_numbers = set()
text_receiver_numbers = set()

for call in calls:
    calling_numbers.add(call[0])
    receiving_numbers.add(call[1])

for text in texts:
    text_sender_numbers.add(text[0])
    text_receiver_numbers.add(text[1])
    
for calling_number in calling_numbers:
    if calling_number not in receiving_numbers and calling_number not in text_sender_numbers and calling_number not in text_receiver_numbers:
        possible_telemarketers.add(calling_number)
    
print("These numbers could be telemarketers: ")
for tele in sorted(possible_telemarketers):
    print(tele)