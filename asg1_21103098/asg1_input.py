#Assignment 1(input)

#Question1
#taking input from user
print("Question 1")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
d=(num1+num2+num3)/3    #calculating average
print("Average of three numbers is: ",d)



#Question2
print("Question 2")
a=int(input("Enter your Gross Income(in nearest penny): $"))  #taking gross income input from user
b=int(input("Enter number of your Dependents: "))  #number of dependents given by user
c=a-10000-(3000*b)  # calculating tax income
Tax=c*0.2  #final tax
print("Your tax is $",Tax)



#Question3
print("Question 3")
#making the student profile list
SID=21103098
Name="Akshit Narang"
Gender="M"
Course_name="CSE"
CGPA=9.5
std_profile=[SID,Name,Gender,Course_name,CGPA]
print(std_profile)



#Question4
print("Question 4")
#Taking marks from each student
std1=int(input("Enter marks of 1st student: "))
std2=int(input("Enter marks of 2nd student: "))
std3=int(input("Enter marks of 3rd student: "))
std4=int(input("Enter marks of 4th student: "))
std5=int(input("Enter marks of 5th student: "))
#presenting these marks in a list and sorting them
marks_list=[std1,std2,std3,std4,std5]
marks_list.sort()
print("Sorted list (increasing order)")
print(marks_list)
marks_list.reverse()
print("Sorted list (decreasing order)",)
print(marks_list)



#Question5a)
print("Question 5 a)")
color_list = ['Red','Green','White','Black','Pink','Yellow']  #making list of some colors
color_list.remove('Black')  #deleting black color from list
print(color_list)



#Question5b)
print("Question 5 b)")
color_list = ['Red','Green','White','Black','Pink','Yellow']
color_list[3:5]=['Purple']  #replacing black and pink to purple
print(color_list)




