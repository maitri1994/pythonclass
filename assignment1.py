import re

def one(num1,num2):

    sum = num1 + num2
    if(sum>100):
        return num1*num2
    else:
        return sum

def two(range1):

    sum = 0
    prev = 0
    for i in range(number+1):
        sum = prev + i
        prev = i
        print(sum)

def three(str):

    for i in range(len(str)):
        if i%2 ==1:
            print (str[i])

def four(str, number):

    print(str[number:])

def five(l1):

    if l1[0] == l1[len(l1)-1]:
        print ("True")

def six(l2):

    new_list=[i for i in l2 if int(i)%2==0 ]
    print(new_list)

def seven(s2):

    count=0
    new_list = re.split(r'\s', s2)

    for pattern in new_list:
        if pattern == "John":
            count = count + 1
    
    print(count)

def eight(n):

    for i in range(0,n):

        for j in range(0, i+1):

            print("*",end="")

        print("\r")

def nine(number):

    revs_number = 0
    number2 = number
    while(number > 0):
        remainder = number%10
        revs_number = (revs_number * 10) + remainder
        number = number//10

    if number2 == revs_number:
        print("number and its reverse is same")
    elif number2!= revs_number:
        print("number and its reverse is not same")


def ten(list1, list2):

    new_list1=[i for i in list1 if int(i)%2==0 ]
    new_list2=[i for i in list2 if int(i)%2==1 ]

    final_list = new_list1 + new_list2
    print(final_list)    

        
        

    


#one
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(one(num1,num2))

#two
number = int(input("Enter range:"))
two(range)

#three
s1 = input("Enter the string:")
three(s1)

#four
s1 = input("Enter the string:")
n = int(input("Enter the integer"))
four(s1,n+1)

#five
l1 = input("Enter the list:")
five(l1)

#six
input_string = input("Enter the list:")
six(input_string)

#seven
input_string = input("Enter the string:")
seven(input_string)

#eight
eight(5)

#nine
number = int(input("Enter the integer number:"))
nine(number)

#ten
input_string1 = input("Enter the list1:")
input_string2 = input("Enter the list2:")
ten(input_string1,input_string2)