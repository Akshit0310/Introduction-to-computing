#Question1
print("Question 1")
a=str(input("Enter any string: "))
a=a.lower()
list=a.split() #spliting all elements in string
dict={} #creating an empty dictionary
if(list.__len__()==1):   #if statement will be implemented when a single word is entered
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   #else statement eill be implemented when more than one word is entered in a string
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n\n")



#Question2
print("Question 2")
def start():#creating a starting function
    #Taking imput from user about day,manth,year
    #a=day, b=month, c=year
    a = int(input("Enter the day:"))#day
    if(a<=0 or a>=31):
        print("Invalid day")
        print("Taking you back to options")
        start()
    else:
        pass

    b=int(input("Enter the month:"))#month
    if(b<=0 or b>=12):
        print("Invalid date")
        print("Taking you back to options")
        start()
    elif(a==31 and (b==2 or b==4 or b==6 or b==9 or b==11)):
        print("Invalid date")
        print("Taking you back to options")
        start()
    elif(a==30 and b==2):
        print("Invalid date")
        print("Taking you back to options")
        start()
    else:
        pass

    c = int(input("Enter the year:"))#year
    if(c<1800 or c>2025):
        print("Please enter the year between 1800 and 2025")
        print("Taking you back to options")
        start()
    elif(b==1 or b==3 or b==5 or b==7 or b==8 or b==10):
        if(a>31):
            print("Invalid date")
            print("Taking you back to options")
            start()
        elif(a<31):
            a+=1
            print("Next date is %d/%d/%d"%(a,b,c))
        elif(a==31):
            a=1
            b+=1
            print("Next date is %d/%d/%d" %(a, b, c))
    elif(b==2 and a<28):
        a+=1
        print("Next date is %d/%d/%d"%(a,b,c))
    elif (b==2 and a==28 and c%4!=0):
        a=1
        b+=1
        print("Next date is %d/%d/%d" % (a, b, c))
    elif(b==2 and a==28 and c%4==0 and c%100!=0):
        a+=1
        print("Next date is %d/%d/%d" % (a, b, c))
    elif(b==2 and a==29 and c%4!=0):#Leap does does not exist in years not divisible by 4
        print("Invalid date(This is not a leap year)")
        print("Taking you back to options")
        start()
    elif(c%100==0 and b==2):
        if(c%400==0 and a==29):
            a=1
            b+=1
            print("Next date is %d/%d/%d" % (a, b, c))
        elif(c%400==0 and a==28):
            a+=1
            print("Next date is %d/%d/%d" % (a, b, c))
        elif(c%400!=0 and a==29):#Leap year does not exist in years divisible by 100 except divisible by 400
            print("Invalid date(Leap year does not exist in years divisible by 100 except if its divisible by 400")
            print("Taking you back to options")
            start()
        elif(c%400!=0 and a==28):
            a=1
            b+=1
            print("Next date is %d/%d/%d" %(a, b, c))
    elif(c%100!=0 and c%4==0 and b==2 and a==29):
        a=1
        b+=1
        print("Next date is %d/%d/%d"%(a,b,c))
    elif(b==4 or b==6 or b==9 or b==11):
        if(a>30):
            print("Invalid date")
            print("Taking you back to options")
            start()
        elif(a<30):
            a+=1
            print("Next date is %d/%d/%d"%(a,b,c))
        elif(a==30):
            a=1
            b+=1
            print("Next date is %d/%d/%d"%(a,b,c))
    elif(b==12):
        if(a>31):
            print("Invalid date")
            print("Taking you back to options")
            start()
        elif(a<31):
            a+=1
            print("Next date is %d/%d/%d"%(a,b,c))
        elif(a==31):
            a=1
            b=1
            c+=1
            print("Next date is %d/%d/%d"%(a,b,c))
    else:#Implementing an extra else just in case
        print("Invalid date")
        print("Taking you back to options")
        start()
start()#calling the fuction
print("\n\n")




#Question3
print("Question 3")
inputlist = input('Enter elements of a list separated by space:\n ')
user_list = inputlist.split()
# print list
print('list: ',inputlist)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
squarelist =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]

print(squarelist)

print("\n\n")


#Question4
print("Question 4")

def input_point():
    point = int(input("Enter grade points: "))
    # check if the grade point meets the conditions
    if point>10 or point<4:
        print("Invalid grade point! Try Again")
        point = input_point()
    return point
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n\n")


#Question5
print("Question 5")
x = 6
for i in range(x):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n\n")

#Question6
print("Question 6")
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("<a>",students)

#part b. sort acc to the names
print("<b>",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c>",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("<d>",students[sid])
print("\n\n")

#Question7
print("Question 7")
#  Function to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("Enter the number of terms of the series: "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("Average of reultant Fibonacci series is ",avg)
print("\n\n")

#Question8
print("Question 8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)
