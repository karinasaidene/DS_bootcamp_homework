def fact(n):
    if n>=0:
        resultat=1;
        if n==0 : return resultat
        else :
            for i in range(1,n+1):
                resultat=resultat*i;
        return resultat;
#test 
print(fact(3))