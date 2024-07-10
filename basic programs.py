'''a = 100
b = 10.5
c = a +b
print(type(c))'''
#explict
'''a=100
a=float(a)
print(type(a))
print(a)'''
#ASCII values
'''char_a = 'A'
char_b = 'B'
ascii_value_a = ord(char_a)
ascii_value_b = ord(char_b)
print("A:",ascii_value_a)
print("B:",ascii_value_b)
ascii_value=65
character=chr(ascii_value)
print("65:",character)'''
#arithmetic operators
'''a = 10
b= 15
print(a+b)'''
#assignment operators
'''y = 5
y+=3
print(y)'''
#comparison operators
'''a= 10
b=20
print(a!=b)'''
#Logical operators
'''a = 1
b = 0
print(a and b)'''
#membership operators
'''
t = [1,2,3]
print(1 in t)
print(4 not in t)'''
#identity operators
'''a = "pgs"
b =  "praveen"
c= "pgs"
print(a is not b)
print(b is c)
print(a is c)'''
#bitwise operators
'''a = 5
b = 6
print(a & b)'''
#Examplecode
'''name = input("Enter your name:")
Age = int(input("Enter your age"))
print("Hello,"+name+"!your age is",Age,"old")'''
#output
'''t = (1,2,3,4)
print(*t)
a = int(input())
b = int(input())
print(a,b,a,b,sep=",",end = "ended here")'''
#ex1
'''name=input()
print("Hello,",name,"!")'''
#ex2
'''n=int(input())
print("you entered",n)'''
#ex3
'''pi=float(input())
print("value of pi",pi)'''
#ex4
'''n = input()
x,y,z = n.split()
sum = int(x)+int(y)+int(z)
print(sum)'''
#ex5
'''n = input()
name,age=n.split(",")
print("Name:",name,",Age:",age)'''
#ex6
'''n = int(input())
print("countdown:54321, ",end = "Blasted off")'''
#ex7
'''n=input()
a,b = n.split()
a = int(a)
b=int(b)
print("Addition:",a+b,"subtraction:",a-b,"multiplication:",a*b,"division:",a/b)'''
#comparison operators
'''x,y = input().split(",")
x = int(x)
y=int(y)
print("10>5",x>y)'''
#logical operators
'''a,b = input().split(",")
print("True and False:",a and b)'''
#f strings
'''name,age = input().split(",")
print(f"Name:{name},Age:{age}old")'''
#1.Find the sum of two numbers
'''
num1,num2=input().split(",")
sum = int(num1)+int(num2)
print(sum)'''
#2.finding the area of circle
'''radius=int(input())
area= 3.14*radius*radius
print(area)'''
#solving quadratic equations
'''a=int(input())
b=int(input())
c=int(input())
root1=0
root2=0
d = (b**2)-(4*a*c)
root1=(-b+(d**(0.5)))/2*a
root2=(-b-(d**(0.5)))/2*a
print(f"roots:{(root1,root2)}")'''
#swap the values of two variables
'''a = 10
b=20
temp=b
b=a
a =temp
print(a)
print(b)'''
#without temp
'''a =10
b= 20
b =b-a
a=a+b
print(a)
print(b)'''
#converting temperature units
'''c =int(input("temperature celsius="))
f = c*(9/5)+32
k =273+c
print(f)
print(k)'''
#basic currency converter
'''a = int(input("amount in usd"))
b =float(input("exchange rate usdv to eur"))
print("Equivalent amount in Eur:",a*b)'''
#simple calculator
'''a = int(input())
b = int(input())
operator = input()
if operator == "+":
    print(f"Addition is {a+b}")
elif operator == "-":
    print(f"subtraction is {a-b}")
elif operator == "*":
    print(f"multiplication is {a*b}")
elif operator == "/":
    print(f"division is {a/b}")
else:
    print("not valid")'''
    
#strings
#Indexing
'''str = "Python"
print(str[0])
print(str[-1])'''
#Slicing
'''s = "Hello World!"
print(s[1:3])
print(s[:3])
print(s[1:])
print(s[::3])
print(s[:-1])
print(s[1::3])
print(s[::-1])'''
#concatenation
'''a = "Pgs"
b = "Praveen"
print(a+ " " +b)'''
#string length
'''string1 = "Hello World!"
print(len(string1))'''
#string methods
'''s = "Hello World!"
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace('o','e'))
print('pgspraveen'.count('p'))'''
#special character
'''s = 'hello\'s world'
print(s)'''
#problems
#vowel counter
'''s = input()
s1=s.lower()
a = s1.count('a')
e = s1.count('e')
i = s1.count('i')
o = s1.count('o')
u = s1.count('u')
print(f"number of vowels:{a+e+i+o+u}")'''
#Gradecalculator
'''m = int(input("marks in math:"))
s= int(input("marks in science:"))
e= int(input("marks in English:"))
Total_marks = m+s+e
Average_marks =(m+s+e)/3
percentage =(Total_marks/300)*100
grade = " "
if percentage > 90:
    grade = "A+"
elif percentage > 80 and percentage<=90:
    grade = "A"   
elif percentage > 70 and percentage<=80:
    grade = "B"   
elif percentage > 60 and percentage<=70:
    grade = "C"   
else:
    grade = "P"

print(f"Total marks:{Total_marks}\nAverage marks:{Average_marks}\ngrade:{grade}")
'''
#palindrome checker
'''r = input()
if r == r[::-1]:
    print("it is a palindrome")
else:
    print("not")'''
#Largest of three numbers
'''a = input()
x,y,z = a.split()
x = int(x)
y = int(y)
z = int(z)
g=0
if x>y:
    if x>z:
        g=(x)
    else:
        g=(z)
elif y>x:
    if y>z:
        g=(y)
    else:
        g=(z)
elif z>x:
    if z>y:
        g=(z)
    else:
        g=(y)
else:
    print("ALLsame")
print("The largest number is",g)'''
#leapyearchecker
'''year = int(input())
leap =""
if year%100 ==0 and year%400!=0:
    leap="False"
elif year%4==0:
    leap="True"
else:
    leap = "False"

print(leap)'''
#temperature converter
'''t = int(input("enter temperature"))
u =(input("enter units"))
if u == "f":
    f = t*(9/5)+32
    print(f)
elif u == "k":
    k = 273.5+t
    print(k)
else:
    print(t)'''
#loops
#while
'''candies = 10
while candies>0:
    print("give candy")
    candies-=1
print("candies")'''
#for
'''candies = int(input())
for i in range(0,candies):
    print("give candies:",i)'''
#for loop for sequence
'''message = "Hello,World!"
for i in message:
    print(i)'''
#ex2
'''message = "Hello,World!"
length = len(message)
for i in range(length):
    print(i)
print(length)'''
#nested loops
'''for i in range(1,6):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")'''
#break
'''candies = int(input())
for i in range(1,candies):
    print("give candie")
    if candies-i == 5:
        print("enough")
        break'''
#continue
'''candies = 10
for i in range(candies):
    if candies-i == 5:
        print("only 5 candies left")
        continue
        print("giving a candy")'''
#problems
#print numbers from 1 to N
'''N = int(input())
i=1
while i<=N:
    print(i)
    i+=1'''
#2
'''c=10
while c>0:
    print(c)
    c-=1'''
#3
'''N=int(input())
for i in range(1,N+1):
    print(i)
    i+=1'''
#calculate the sum of n natural numbers
'''n = int(input())
i = 1
sum=0
for i in range(1,n+1):
    sum+=i
    
print(sum)'''
#print even and odd numbers
'''n=int(input())
i=0
for i in range(0,n+1):
    if (i%2)=0:
        print(i)'''
#multiplication table of n from 1 to 10
'''n = int(input())
for i in range(1,11):
    print(f"{n}*{i}={n*i}")'''
#factorial of a number
'''n = int(input())
fact=1
for i in range(1,n+1):
    
    fact*=i
    i-=1
print(fact)'''
#Functions
#return statement#positional arguments
'''def add(a,b):
    return a+b
result = add(3,2)
print(result)'''
#keyword arguments
'''def personalinfo(name,age):
    print("name",name)
    print("age",age)
personalinfo("praveen",21)'''
#Default arguments
'''def greet(name,greeti="hello"):
    return greeti + ","+name+"!"  
greeting1 =greet("pgs")
greeting2=greet("praveen","HI")
print(greeting1)
print(greeting2)'''
#scope of variables
#globalscope
'''global_var = 10
def my_function():
    print(global_var)'''
#localscope
'''def my_function():
    local_var=5
    print(local_var)
my_function()'''    
#lambda function
'''add = lambda x,y:x+y
result =add(3,5)
print(result)'''
#problems
#sum of numbers
'''def add(a,b):
    print(a+b)
add(3,4)'''
#area of circle
'''r = int(input())
def area(r):
    print(3.14*r*r)
area(r)'''
#solving quadratic equations
'''a = int(input())
b=int(input())
c=int(input())
def quadratic(a,b,c):
    print(f"Roots:{root1,root2}")
d = ((b**2)-4*a*c)
root1= (-b+d**0.5)/2*a
root2= (-b-d**0.5)/2*a
quadratic(a,b,c)'''
#swap the values of two variables without temp
'''def swap(a,b):
    b=b+a
    a=b-a
    b=b-a
    print(a)
    print(b)
swap(5,10)'''
#Lists
#accessing elements
'''fruits =["orange","grapes","banana"]
print(fruits)
print(fruits[0])
print(fruits[-1])'''
#slicing lists
'''fruits =["orange","grapes","banana","guava","mango"]
print(fruits[1:5])'''
#modifying elements
'''fruits =["orange","grapes","banana","guava","mango"]
fruits[0]="apple"
print(fruits)'''
#methods
'''l=[12,1,2,3,4,5,8,6,7,8]
l.append(9)
l.insert(0,5)
l.remove(5)
l.pop()
print(l.index(4))
print(l.count(5))
l.sort()
l.reverse()
print(l)'''
#list concatenation
'''l1=[1,2,3]
l2=[3,4,5]
l3=l1+l2
print(l3)'''
#list comprehension
'''squares =[x**2 for x in range(1,6)]
print(squares)'''
'''a = input().split()
l = [int(item) for item in a]
print(l)'''
#tuples
'''my_tuple = (10,20,30,10)
print(my_tuple[0])
c=my_tuple.count(10)
print(c)
i=my_tuple.index(10)
print(i)'''
#sets
'''empty_set = set()
fruits ={"apple","banana","cherry"}
numbers=set([1,2,3,4,5])'''
#Adding elements
'''s ={1,2,3}
s.add(4)
print(s)'''
#remove
'''s={1,2,3}
s.remove(3)
print(s)'''
#set operations
'''s1={1,2,3,4,5}
s2={4,5,6,7,8}
union =s1.union(s2)
i =s1.intersection(s2)
d =s1.difference(s2)
s =s1.symmetric_difference(s2)
print(union)
print(i)
print(d)
print(s)'''
#set membership
'''ms ={1,2,3}
print(1 in ms)
print(2 not in ms)'''
#frozensets
'''my_set ={1,2,3}
frozen_set = frozenset(my_set)
print(frozen_set)'''
#set comprehension
'''square ={x**2 for x in range(1,6)}
print(square)'''
#set methods
'''my_set ={1,2,3}
my_set.clear()
print(my_set)'''
'''my_set ={1,2,3}
new_set=my_set.copy()
print(new_set)'''
'''my_set ={1,2,3}
my_set.update([4,5,6])
print(my_set)'''
#dictionary
#accessing values
'''my_dict={'name':'pgs','age':21,'house':'mdp'}
print(my_dict['name'])
print(my_dict['age'])'''
#adding values
'''my_dict={'name':'pgs',1:2,'house':'mdp'}
my_dict['gender']='male'
print(my_dict.get(1))
print(my_dict.pop('name'))
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict)'''
#loops in dictionary
'''my_dict={'name':'pgs',1:2,'house':'mdp'}
for value in my_dict.values():
    print(value)
for key in my_dict.keys():
    print(key)
for item in my_dict.items():
    print(item)'''
#dict comprehensions
'''squares_dict ={x:x**2 for x in range(1,8)}
print(squares_dict)'''
#problems
#sum of list
'''l=[1,2,3,4,56]
s=0
for x in l:
    s+=x
print(s)'''
#method 2
'''l=[1,2,3,4,56]
s=0
i=0
l1=len(l)
while i<l1 :
    s+=l[i]
    i+=1
print(s)'''
#find maxi and mini values in a list
'''l= [15,2,7,25,10]
l.sort()
print(l)
print(l[0])
print(l[-1])'''
#method 2 create
'''num = int(input())
l=[]
for n in range(num):
    nu=int(input())
    l.append(nu)
print(l)
print(max(l))
print(min(l))'''
#method3 with functions
'''def minandmax():
    l=[5,8,3,1,9]
    min=l[0]
    max=l[0]
    for i in l:
        if i>max:
            max=i
        elif i<min:
            min=i
    print("max",max)
    print("min",min)
minandmax()'''
#Remove duplicate elements from a list
'''a = input().split(",")
l=[int(item) for item in a]
newl=[]
for i in l:
    if i in newl:
        continue
    else:
        newl.append(i)
print(newl)'''
#method2
'''a =input().split(",")
l=[int(x) for x in a]
s=set(l)
print(list(s))'''
#count the number of occurences of a specific element in list
'''a = input().split(",")
l=[int(item) for item in a]
n=int(input())
count =0
for i in l:
    if i == n:
        count=count+1
print(count)'''
#create dictionaries
'''my_dict1 ={}
my_dict2={}
a =input()
b=input()
c=input()
d=input()
my_dict1["name "]=a
my_dict1["age "]=b
my_dict1["city "]=c
my_dict2["city "]=d
my_dict1.update(my_dict2)
print(my_dict1)'''
#ex
'''dict={'name':'pgs','age':21,'city':'mdp'}
dict.update({'age':22,'city':'rjy'})
for i,j in dict.items():
    print(f"{i}:{j}")'''
#recursive function factorial

'''def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)        
print(fact(3))'''
#fibonacci series
'''def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1        
    else:
        return fib(n-1)+fib(n-2)
print(fib(4))'''
#without parameter,without return value
'''a=5
b=6
def add():
    global a,b,result
    result = a+b
add()
print(result)'''
#without parameter,with return value
'''a=5
b=6
def add():
    global a,b
    return a+b
result =add()
print(result)'''
#with parameter,without return value
'''def add(a,b):
    print(a+b)
add(5,6)'''
#with parameter,with return value
'''def add(a,b):
    return a+b
result = add(3,5)
print(result)'''
    


   


