# Maternity #
# December 09, 2018
# By Robin Nash

alice = input()
bob = input()

alice = [alice[i:i+2] for i in range(0,10,2)]
bob = [bob[i:i+2] for i in range(0,10,2)]

# e for either, r for recessive, d for dominant
genes = []
for pair in range(5):
    bobp = bob[pair]
    alicep = alice[pair]

    if bobp.islower() and alicep.islower():
        genes.append('r')
    elif bobp.isupper() or alicep.isupper():
        genes.append('d')
    else:
        genes.append('e')
    

for t in range(int(input())):
    baby = input()
    babyTheirs = True
    for i in range(5):
        babya = baby[i]
        if babya.islower():
            if genes[i] == 'd':
                babyTheirs = False
        else:
            if genes[i] == 'r':
                babyTheirs = False
    if babyTheirs:
        print('Possible baby.')
    else:
        print('Not their baby!')
        
        

        
            
            
            
        
#1544393296.0