
#Question1
input_string="Python is a case sensitive language"
#a)part
print("Part A!")
print("Length os input string", len(input_string)) #The length of input string


#b)part
print("\nPart B!")
print("Reverse of string is", "'" + input_string[::-1] + "'") #Reversing the input string


#c)part
print("\nPart C!")
slicestr = input_string[slice(9, 26)] #creating a new string
print(slicestr)


#d)part
print("\nPart D!")
newstring = input_string.replace("a case sensitive", "object oriented") #replacing 'a case sensitive' from 'object orientated'
print(newstring)


#e)part
print("\nPart E!")
print("Index of substring 'a' is", input_string.index('a')) #Printing the index of a in input string


#f)part
print("\nPart F!")
print(input_string.replace(" ", "")) #Removing all the blank spaces between words in input string



#Question 2

#Taking input from user
name = input("Please enter your name: ")
sid = input("Enter SID: ")
dep = input("Enter department name: ")
cgpa = float(input("Enter CGPA: "))
print("\n\n Hey, "+ name +" Here!")        #printing according to question
print("     My SID is ", sid)
print("     I am from " + dep + " department and my CGPA is ",cgpa)


#Question3

a=56
b=10
#a) part
print("Part A!")
print("a&b: ",a&b)


#b)part
print("\n\nPart B!")
print("a|b: ",a|b)


#c)part
print("\n\nPart C!")
print("a^b: ",a^b)


#d)part
print("\n\nPart D!")
print("a<<2:",a<<2,"\nb<<2: ",  b<<2)


#e)part
print("\n\nPart E!")
print("a>>2:",a>>2, "\nb>>4:",b>>4)


#Question4

m = []
#taking numbers from user
num_1=float(input("Enter 1st number: "))
num_2=float(input("Enter 2nd number: "))
num_3=float(input("Enter 3rd number: "))

#making a list of all the numbers
m.append(num_1)
m.append(num_2)
m.append(num_3)

m.sort()
m.reverse()
print("The greatest value is:", m[0]) #printig the greatest number


#Question5

inp_string = input("Enter the string: ")
if 'name' in inp_string:
    print("yes")

else:
    print("no")


#Question6

#Taking sides from user
side_1=int(input("Enter 1st side: "))
side_2=int(input("Enter 2nd side: "))
side_3=int(input("Enter 3rd side: "))

#printing whether the numbers entered can form a triangle or not
if (side_1>side_2+side_3 or side_2>side_1+side_3 or side_3>side_2+side_1):
    print("No")
else :
    print("Yes")
