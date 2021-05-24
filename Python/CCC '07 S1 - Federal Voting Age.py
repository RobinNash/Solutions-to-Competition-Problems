# Federal Voting Age #
# August 20, 2019
# By Robin Nash

def isEligible(date):
    vy, vm, vd = [int(i) for i in date.split()] #vy for voter year, vm voter month
    ey, em, ed = 2007, 2, 27 #election year, election month ...

    # Exactly 18 years is 1989, 2, 27
    
    if vy > 1989:
        return False

    if vy < 1989:
        return True
    
    # If year is 1989
    if vm > 2:
        return False
    
    if vd > 27 and vm == 2:
        return False

    return True

dates = int(input())
for i in range(dates):
    date = input()
    if isEligible(date):
        print("Yes")
    else:
        print("No")

    
    
#1566326006.0