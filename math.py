import time
print("QUADRATIC EQUATION")
time.sleep(1)
print("\nQUADRATIC FORMULA\na²+bx+c")
time.sleep(1)
print("\nDiscriminant\nD=b²-4ac")
time.sleep(1)
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
#print("Your Quadratic Formula Looks like\n",pow(a**2),"+",b,+"+","x","+",c)
d = (b**2)-(4*a*c)
print("D=", d)
sol1 = (-b+d**0.5/2*a)
sol2 = (b-d**0.5/2*a)
sol3 = (-b/2*a)
if d == 0:
    print("Answer of your Quadratic Equation is=", sol3)
elif d>= 0:
    print("Answers of your Quadratic Euqation are=", sol1, "and", sol2)
else:
    print("Your Quadratic Equation is lower than 0.")