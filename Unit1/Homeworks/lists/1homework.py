import math
my_list=[]
for i in range(2,300,2):
      my_list.append(i);

print("the length of the list is ",len(my_list))    

for x in my_list:
   if (int(math.sqrt(x)+0.5)**2)==x:
         print("this a squared value of the list",x)

print("57 is in the list :",57 in my_list)
