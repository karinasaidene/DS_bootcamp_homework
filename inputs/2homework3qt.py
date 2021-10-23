file=open('./inputs/student_names.txt',"r");
#read first nb_lign
students=file.read();
#check if Jane Smith is in the file

if 'Jane Smith' in students:
    print("found !")
else:
    print("not found !")

file.close();