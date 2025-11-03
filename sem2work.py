#Q1.Write a Python program to perform arithmetic operations (addition, subtraction, multiplication, and division) on two variables.

a=1000
b=900
print("numbers are 1000 and 900")
print("a+b=",a+b)
print("a-b=",a-b)
print("a x b=",a*b)
print("a/b=",a/b)

#Q2.Write a Python program to demonstrate variable assignment by storing a number and a string in variables and then printing them together.

no=1
name="only nikhitha"
print(no,"and",name)


#Q3.Write a Python program to print the names of three economists, each on a separate line.

print("the Three Economists are:")
print("Alfred Marshall")
print("Milton Friedman")
print("Adam Smith")

#Q4.Write a Python program to split a given quote into individual words and print each word on a new line.

quote="What you seek is seeking you -Rumi"
for i in quote.split():
    print(i)

#Q5.Write a Python program to convert a given list into a tuple and then print both the original list and the converted tuple.
    
list1=["Love","is","the","sea","where","intellect","drowns","-Rumi"]
tuple1=tuple(list1)
print(list1)
print(tuple1)


#Q6.Write a Python program to extract and print a specific word ("reflection") from a given list using slicing.

words = ["The","beauty","you","see","in","me","is","the","reflection","of","you","again","Rumi"]
r=words[8:9]  
print(r)

#Q7.Write a Python program to compare two numbers using if-elif statements and print the relationship between them (equal, not equal, greater than, less than).

x=100
y=200
if x==y:
    print("x is equal to y")
elif x!=y:
    print("x is not equal to y")
elif x>y:
    print("x is greater than y")
elif x<y:
    print("y is greater than x")

#Q8.Write a Python function that takes two parameters, multiplies them, and prints the result.

def multiply(a,b):
    c=a*b
    print(c)
multiply(2,3)

#Q9.Write a Python function that takes a number as input, calculates its square, and returns the result.

def niki(x):
    return x**2 + 6
print(niki(3))

#Q10.Write a Python function that determines a person's profile ("entrepreneur", "investor", or "employee") based on their income, business ownership status, and investment status.

def who_am_i(income, ownbusiness, investments):
    if income>50000 and ownbusiness==True:
        return "entrepreneur"
    elif investments==True and ownbusiness==False:
        return "Investor"
    else:
        return "Employee"
print(who_am_i(50000, False, True))
print(who_am_i(60000, True, True))
print(who_am_i(30000, True, True))

#Q11.Write a Python function that takes no parameters and prints a feedback message when called.



def feedback():
    print("Classes are nice")
feedback()