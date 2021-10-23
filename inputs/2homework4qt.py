# generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
for i in range(97, 123):
    print(chr(i))
    open('./inputs/'+chr(i)+'.txt',"w+")