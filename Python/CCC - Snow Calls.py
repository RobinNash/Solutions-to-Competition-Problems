# Snow Calls #
# November 12, 2018
# By Robin Nash

alpha = ['',"","ABC","DEF","GHI",'JKL','MNO','PQRS',"TUV","WXYZ"]

for t in range(int(input())):
    sequence = [i for i in input() if i != "-"]
    numbers=[]
    for i in sequence:
        number = i
        for ii in alpha:
            if i in ii:
                number = alpha.index(ii)
        numbers.append(number)
    for i in range(10):
        print(numbers[i],end='')
        if i in [2,5]:
            print("-",end="")
    print()
                
                
        
#1541984300.0