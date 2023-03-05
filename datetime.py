# import datetime
# import time
#import calendar
import math
# print(dir(datetime))
# #import datetime
#
# x = datetime.datetime.
# print(x)

# import datetime
#
# print(datetime.datetime(2020, 5, 17))
#
# #print(x)

#print(time.localtime(time.time()))
#print(dir())

# for i in range(5,0,-1):
#     print(i, end=", ")

# for i in range(5,5,-1):
#     print(i, end=", ")

# for i in reversed(range(10, 20)):
#     print(i, end=' ')
# print(type(range(0, 5)))
# # Output <class 'range'>
#
# print(type(reversed(range(0, 5))))

# list1 = [10, 20, 30, 40, 50]
# # start = list's size
# # stop = -1
# # step = -1
#
# # reverse a list
# for i in range(len(list1)-1, -1, -1):
#     print(list1[i], end=" ")

    # Decrement range() using step
    # start = 30, stop = 20
    # step = -2
# for i in range(30, 20, -2):
#         print(i, end=' ')

#returned by the range() inside the square brackets.
# create list from range()
sample_list = list(range(2, 10, 2))
print(type(sample_list))
# Output <class 'list'>

# display list
#
# Output [2, 4, 6, 8]

# iterate list
# for item in sample_list:
#     print(item)
for i in range(len(sample_list)):
        print(sample_list[i])