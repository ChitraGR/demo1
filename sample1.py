import os
import datetime
# l1=(1,2,3,4)
# l2=(0,6,7,8)
# l3=zip(l1,l2)
# print(dict(l3))

# l1={1:2,4:6}
# l2={4:9,5:0}
# l3=zip(l1,l2)
# print(set(l3))
# ptr=open("C:\\Users\\chitra.gr\\Documents\\OC\\OC-links.txt","r")

# for i in ptr:
#     print(i,end="")   #to read full file

# con=ptr.read(10) #here 10 is number of characters to be read from file, reads first 10 characters
# print(con)

# con1=ptr.readline() #reads single line, line1
# con2=ptr.readline() #reads single line, line2
# print(con1,con2)
# ptr.close()

# con_full=ptr.readlines() #reads ll lines till end of file, output in list format
# print(con_full)
# ptr.close()ask
# def myfunc(n):
#   return lambda a : a * n

# my1 = myfunc(2)
# mytripler = myfunc(3)
#
# print(my1(11))
# print(mytripler(11))

# def myfunc(n):
#   return lambda a : a * n
# b=myfunc(4)
# print(b(8))

# x = lambda a : a + 10
# print(x(5))

# username = input("Enter username:")
# print("Username is: " + username)

# creating an empty list
# lst = []
#
# # number of elements as input
# n = int(input("Enter number of elements : "))
#
# # iterating till the range
# for i in range(0, n):
#   #ele = int(input())
#
#   lst.append(i)  # adding the element
#
# print(lst)

# lst = []
#
# # number of elements as input
# n = int(input("Enter number of elements : "))
# lst.append(n)
# print(lst)
#h="fKLhj vnu hk kh"
#print(h.strip())
#print(h.r())

# s="hi,welcome"
# print(s.split())
# print(s.split(","))
# print(s.split(" "))
#
# m="hi , welcome"
# print(m.split(","))

# n="hi welcome here"
# print(n.split())
# print(n.split(","))
# print(n.split(" "))

# o="ghjk"
# print(o.split())
# print(o.split(","))

#h="jellolokj"
#print(h.replace("j","m",2))
#del h
# print(h[1])
# m=sorted(h)
# prin
#print

# a=[1,2,4]
# b=[0,8,9]
# c={}
# m=[]
# n=[]
# count=0
# for i in range(len(a)):
#
#     m.append(a[i])
#     count += 1
#     for j in range(len(b)):
#
#         n.append(b[j])
#         count = count + 1
#
# c={m[i]:n[j]}
# print(c)
# n = int(input("enter a n value:"))
# d = {}
#
# for i in range(n):
#     keys = input() # here i have taken keys as strings
#     values = int(input()) # here i have taken values as integers
#     d[keys] = values
# print(d)

# a=(0,8,6)
# print(list(a))

# a=[7,8,9,6,5,78,9]
# #a[:4]=['a','b','c','b']
# a.insert(2,'o')
# print(a)
# a

a=dir(datetime)
print(a)

print(dir(os))
