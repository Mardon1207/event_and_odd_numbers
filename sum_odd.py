#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_odd" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
var_int=int(input())
sum_even=(var_int//1000*((var_int//1000%2)))+(var_int%1000//100*((var_int%1000//100%2)))+(var_int%100//10*((var_int%100//10%2)))+(var_int%10*((var_int%10%2)))
print(sum_even)
