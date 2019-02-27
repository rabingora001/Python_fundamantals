# 1 Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False
# def biggieSize(arr):
#     for i in range(len(arr)):
#         if(arr[i]>0):
#             arr[i]="big"
#     print(arr)
# biggieSize([-1,2,3,-5,6])


# 2# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
# def countPositive(arr):
#     count=0
#     for i in range(len(arr)):
#         if(arr[i]>0):
#             count+=1
#         arr[(len(arr)-1)]=count
#     print(arr)
# countPositive([-1,1,1,1])


# # 3SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
# def sumTotal(arr):
#     sum=0
#     for i in range(len(arr)):
#         sum=sum+arr[i]
#     return sum
# x=sumTotal([1,2,3,4])
# print(x)


# 4 Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
# def average(arr):
#     sum=0
#     ave=0
#     for i in range(len(arr)):
#         sum=sum+arr[i]
#     ave=sum/len(arr)
#     return ave
# average([1,2,3,4])

# 5 Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
# def length(arr):
#     print(len(arr))
# length([1,2,3,4,7,8])

# 7 Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
# def minimum(arr):
#     if(len(arr)==0):
#         return False
#     else:
#         min=arr[0]
#         for i in range(len(arr)):
#             if (arr[i]<min):
#                 min=arr[i]
#         print(min)
# minimum([])


# 8 Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
# def maximum(arr):
#     if(len(arr)==0):
#         return False
#     else:
#         max=arr[0]
#         for i in range(len(arr)):
#             if (arr[i]>max):
#                 max=arr[i]
#         print(max)
# maximum([-1,-2,-4])


# 9 UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
# def ultimateAnalyze(arr):
#         max=arr[0]
#         min=arr[0]
#         sumTotal=0
#         avg=0
#         ult={}
#         for i in range(len(arr)):
#             if (arr[i]>max):
#                 max=arr[i]
#             elif(arr[i]<min):
#                 min=arr[i]
#             sumTotal +=arr[i]
#             avg=sumTotal/len(arr)
#         ult={
#             "max" : max,
#             "min" : min,
#             "Total":sumTotal,
#             "Average":avg,
#             "length":len(arr)
#         }
#         print ult
# ultimateAnalyze([1,2,5,6,7])

# 9 ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
# def ReverseList(arr):

