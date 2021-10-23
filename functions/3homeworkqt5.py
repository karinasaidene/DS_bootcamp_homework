def reverse_str(word):
    pos=len(word);
    result=word[pos :: -1];
    return print("reversed word is ",result)

#test 
reverse_str("python")