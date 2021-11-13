def palyndrome(word):
    int_pos=0;
    fin_pos=len(word)-1;
    while(int_pos<=fin_pos):
        if not word[int_pos]==word[fin_pos] :
            return False
        int_pos=int_pos+1;
        fin_pos=fin_pos-1;
    return True   
#test 
print("stats is a palyndromic word ?",palyndrome("stats"))
print("python is a palyndromic word ?",palyndrome("python"))
