

#Find the nth Occurrence of a word in a string!
def find_nth_occurrence(substring, string, occurrence=1):
    try:
        length = len(substring)

        for i in range(len(string)):

            if i == len(string) - 1 and occurrence >= 1:
                return -1

            if string[i] == substring[0]:
                if string[i:i + length] == substring:
                    if occurrence == 1:
                        return i
                    else:
                        occurrence -= 1
                else:
                    continue
    except:
        return "wrong input"


#Simple String Matching

def solve(a,b):
    try:
        index= a.find("*")
        if a=="*":
            return True
        elif index !=-1:
            strip=a.split('*')
            print(strip)
            s= "^"+strip[0]+".+"+strip[1]+"$"
            print (s)
            x = re.search(s, a)
            print(x)
            if x:
                return True
            else:
                return False
        elif index==-1:
            if a==b:
                return True
            else:
                return False
    except:
        print("wrong input")

#Is it a palindrome?
def is_palindrome(s):
    try:
        s=s.lower()
        return s[::-1]==s
    except:
        print("wrong input")

#Repeated Substring (Bonus Question)
def f(s):
    try:
        #list to add the unique elements
        patt=[]
        #looping to add the unique elemnts
        for i in s:
            if i in patt:
                continue
            else:
                patt.append(i)
        #making the substring from list into str
        ans= "".join(patt)
        #counting the repition for the substring in the main string
        count= s.count(ans)
        #handling the case where the substring oly occurs once --> consider the main s as unique
        if count==1:
            return (s,count)
        else:
            return (ans,count)
    except:
        print("wrong input")