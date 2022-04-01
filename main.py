import re
import string_ops

print("hello there.. wanna try few functions using strings??")
print('''you can use one of the following 4:
a.	Find the nth Occurrence of a word in a string!
b.	Simple String Matching
c.	Is it a palindrome?
d.	Repeated Substring 
just write the function's number and click enter ;)''')

while True:
    inp= input()
    if inp=="a":
        string=input("enter the full string>> ")
        sub=input("enter the word you're looking for>> ")
        occ=1
        try:
            occ= int(input("enter the occurrence number>> "))
        except:
            print("wrong input")
        print(string_ops.find_nth_occurrence(sub,string,occ))

    elif inp =="b":
        a=input("enter the first string>> ")
        b= input("enter the second string>> ")
        print(string_ops.solve(a,b))

    elif inp=="c":
        s=input("enter a string to check if it's palindrome>> ")
        print(string_ops.is_palindrome(s))
    elif inp=="d":
        s=input("plz enter the string you want to check the repeated substring in>> ")
        print(string_ops.f(s))
    else:
        print("are u sure u entered the right letter? try again")