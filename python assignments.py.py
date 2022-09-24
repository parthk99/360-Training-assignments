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
