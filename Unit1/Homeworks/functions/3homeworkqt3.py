def test_range(n,a,b):
    if n in range(a,b):
         print( " %s is in the range"%str(n))
    else:
         print( " %s is  NOT in the range"%str(n))

#test
test_range(5, 3, 9)
test_range(12, 3, 9)