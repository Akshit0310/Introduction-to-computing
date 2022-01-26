
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
