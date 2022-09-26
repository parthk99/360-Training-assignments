#Exercise 1.1
a, b, c = 1, 2.01, "String"
print(a,b,c)

#Exercise 1.2
x = 1 + 2j
print(int(x))
print(x)

#Exercise 1.3
x = 10
y =20 
print(x,y)
x , y = y, x 
print(x,y)

#Exercise 1.4
user = input("What is your name? ")
print("hello", user)

#Exercise 1.5
num1 = input("Enter any number between 1-10 ")
num2 = input("Enter another number between 1-10 ")
z = int(num1) + int(num2)
sum = int(z + 30)
print(sum)

#Exercise 1.6
x = "Hello"
print(type(x))

#Exercise 1.7
#uppercamelcase = MyCar
#lowercamelcase = myCar
#uppercase = MYCAR  
#snakecase = my_car

#Exercise 1.8
#yes, because the memory location for the original value will be overridden by the new value and the pointer will be pointed towards the new value. 

#Exercise 2.1
num=int(input("Enter your number:"))
if num%3==0:
    print("consultadd")
else:
    print()

num=int(input("Enter your number:"))
if num%5==0:
    print("Python Training")
else:
    print()

num=int(input("Enter your number:"))
if num%3==0 and num%5==0:
    print("consultadd - Python Training")
else:
    print()

#Exercise 2.2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
choice = input("Pick a operation: 1=Addition, 2=Subtraction, 3=Multiplication, 4=Division, 5=Avg; ")
result = 0 
if choice == "1":
    result = num1 + num2
    if result < 0:
        print("negative")
        print("Answer after adding is: ", result)
elif choice == "2":
    result = num1 - num2
    if result < 0:
        print("negative")
    print("Answer after subtracting is: ", result)
elif choice == "3":
    result = num1 * num2
    if result < 0:
        print("negative")
    print("Answer after multiplying is: ", result)
elif choice == "4":
    result = num1 / num2
    if result < 0:
        print("negative")
    print("Answer after dividing is: ", result)
elif choice == "5":
    result = num1 + num2 / 2
    if result < 0:
        print("negative")
    print("answer after averaging: ", result)
else : 
    print("Not recognized.")

#Exercises 2.3
#Exercise 2.4
user = int(input("Enter either a positive or a negative number"))
if user <=0:
    print("its over")
if user >0:
    print("Good going")

#Exercise 2.5
x = range(2000, 3201)
for i in x:
    if i%7 == 0 and i%5 != 0: 
         print(i)


# Exercise 2.6(1)
# "int"object is not iterable
# 2.6(2)
# "break" outside loop
# 2.6(3)
# the output is infinite

# Exercise 2.7
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')