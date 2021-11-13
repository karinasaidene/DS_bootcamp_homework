file=open('./inputs/student_names.txt',"r+");
nb_lign=int(input("enter the number of the lines you want to read \t"));
#read first nb_lign
students=file.readlines();
print("the first",nb_lign,"of students");
first_list=students[:nb_lign]
print(first_list)
   

#read last nb_lign
print("the last",nb_lign,"of students");
last_list=students[-nb_lign:]
print(last_list)
file.close()

