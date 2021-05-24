# Simple Encryption #
# October 20, 2018
# By Robin Nash

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

keyword = input()
raw_message = input()
message = ""

for i in raw_message:
    if i in ALPHABET:
        message+=i

segments = []
for i in range(0,len(message),len(keyword)):
    try:
        segments.append(message[i:i+len(keyword)])
    except IndexError:
        segments.append(message[i:])
        break

for ii in range(len(segments)):
    segment=segments[ii]
    seg=""
    for i in range(len(segment)):
        shift = ALPHABET.find(keyword[i])
        seg+= ALPHABET[shift+ALPHABET.find(segment[i])]
    segments[ii]=seg
        

for segment in segments:
    print(segment,end='')






    
#1540073796.0