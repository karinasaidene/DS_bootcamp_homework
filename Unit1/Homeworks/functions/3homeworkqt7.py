#here we use  nested functions
def max(a,b):
    if a>=b :
        return a
    else :
        return b

def max_3_nb(a,b,c):
    return max(max(a,b),c);

#test
print("max between -7 , 4  and 5 is ",max_3_nb (-7,4,5))



