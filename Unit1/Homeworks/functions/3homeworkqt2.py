def prime(num):
    for n in range(2,int(num/2)+1):
        if num%n==0:
            return False
    return True
#test 
print(prime(7))
print(prime(8))