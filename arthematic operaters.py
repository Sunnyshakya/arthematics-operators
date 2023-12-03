# (1) Average of 5 numbers

a = int(input("first number = "))
b = int(input("second number = "))
c = int(input("third number = "))
d = int(input("forth number = "))
e = int(input("fifth number = "))

avg = (a+b+c+d+e)/5
print("avg = ",avg)

# (2) area of circle

r = int(input("radius = "))

area = float(3.14159)*r**2
print(area)


# (3) Calculate simple intrest

p = int(input("principle = " ))
t = int(input("time = "))
r = int(input("rate = "))

SI = (p*t*r)/100
print(SI)

# (4) Calculate the compound intrest

P = int(input("principle = "))

cp = (P*(1+1/100)-P)
print("cp = ", cp)

# (5) Calculate area of rectangle

l = int(input("length = "))
b = int(input("breadth = "))

area = (l*b)
print("area of rectangle = ", area)

# (6) Write a program to calculate circumferance of circle

r = int(input("radius of circle = "))

circumferance = (2*float(3.14159265359)*r)

print("circumferance of circle = ",circumferance)

# (7) kilometer to meter

km = int(input("kilometer = "))
m = (km*1000)

print("meter = ", m)

# (8) meter to centimeter

m = int(input("meter = "))

cm = (m*100)
print("centimeter = ",cm)

# (9) celcius to fahrenheit

c= int(input("celcius = "))
f= (c*9/5+32)

print("fahrenheit = ", f)

# (10) calculate the number after dividing two number

a = int(input("first number = "))
b = int(input("second number = "))

rmd = (a%b)
print("reminder = ",rmd)