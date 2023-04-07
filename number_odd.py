#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".

var_int=int(input())
var_int=(var_int//1000%2)+(var_int//100%2)+(var_int//10%2)+(var_int%2)
print(var_int)
