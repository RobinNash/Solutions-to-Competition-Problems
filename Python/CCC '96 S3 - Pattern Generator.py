# Pattern Generator #
# August 20, 2019
# By Robin Nash

def getBit(bits, ones, pattern = "", patterns = []):
    
    if len(pattern) < bits:
        if pattern.count("1") < ones:
            getBit(bits, ones, pattern + "1",patterns)
        getBit(bits, ones, pattern + "0",patterns)
        
    else:
        if pattern.count("1") == ones:
            patterns.append(pattern)

    return patterns

#inputs = ["2 1", "2 0", "4 2"]

for i in range (int(input())):
    bits, ones = [int(i) for i in input().split()]
    patterns = getBit(bits, ones, "" , [])
    print("The bit patterns are")
    for pattern in patterns:
        print(pattern)
    print()
#1566328814.0