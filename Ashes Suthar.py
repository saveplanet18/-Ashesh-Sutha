
# Write a program that accepts multiple number of sentences as input and prints the lines after making all characters in the sentence capitalized.

def MutipleInput():
    p,q =input("Enter your First String: \n"),input("Enter the Second String:\n").capitalize()
    words = p.upper()
    wordCount = q.upper()
    print(wordCount,words)
MutipleInput()

#2) Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

from collections import OrderedDict

def Duplicat(string):
    word= (' '.join(OrderedDict((w,w) for w in string.split()).keys()))
    told=word.split()
    told.sort()
    return "".join(told)
string="hello world and practice makes perfect and hello world again"
print(Duplicat(string))


#3) We have a count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? Write a program to get the answer,

def RabbitChicken(sum,leg):
    for rabbit in range(sum+1): #According to the first equation:- x+y=34
        chicken=sum-rabbit     #According to the second equation:- 4x +2y=94
        if 2*chicken+4*rabbit==leg: #Multiply the first equation by 2
            return chicken,rabbit
    return None,None

if __name__ == '__main__':
    try:
        heads=int(input("Enter the number of head:\n"))
        legs=int(input("Enter the number of leg:\n"))
        res=RabbitChicken(heads,legs)
        print("number of rabbit %d and number of chicken%d"%res)
    except TypeError:
        print("invalid")


#4) Create a function that accepts single list containing letters or may be words. Total number of elements in a list may vary. In turn, it counts the number of occurrences in a list for each element and returns user a dictionary with total number of counts for each element. Please remember to include case-sensitive match i.e. 'user1' is not equal to 'User1' word.

def show(mylist):
    dict1 = {} # empty dictionary
    for item in mylist:
        if (item in dict1):
            dict1[item] += 1
        else:
            dict1[item] = 1
    for key, value in dict1.items():
        print ("% s : % s"%(key, value))

if __name__ == "__main__":
    mylist =['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1']
    show(mylist)

#5) Create a function that accepts a list containing integers. Total number of elements in list may vary. Your method should return back the list removing duplicates from list. So lets say if user passes a following list to your function as input:


def hack(mylsit):
    res=[]
    for i in mylsit:
        if i not in res:
            res.append(i)
    return res
mylist= [1,2,55,1,3,2,34,55]
print(hack(mylist))