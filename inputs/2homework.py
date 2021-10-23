#Read all of the content of the file in one variable.
file=open('./inputs/student_names.txt',"r+");
students=file.read();
print("this is a list of student's name from the given file \n",students);
#Write a list of random names to the file
random_names=['Anderson Gabriela','Blythe Steven','Costa Sonia','Simone Roy']

for student in random_names :
    file.write(student+'\n');
file.close();
