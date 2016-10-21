#!/usr/bin/python

import sys
import numbers
from compiler.ast import flatten

first_input=raw_input("")
myString=[]
myString, myNum=first_input.split(" ")
ReqNum=int(myNum)
ret_list=[]
my_Dummy='a'

if ReqNum > len(myString):
	print "Please check your input, seems something wrong"
	print "Enter the string and required number.. "
	print "Ex:- abc 3"
	print "Ex:- Output will print all permutations of abc"
	print "Output:- 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'"
	sys.exit(1)


def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        n = n * factorial(n-1)
    return n

def permutation(a, myString):  #  a - dummy in case of first call , b - n distinct objects taken r at a time 
	i=0
	temp_list_2=[]
	if ReqNum == 1:
		temp=list(myString)
		return temp
	elif len(myString) == 2 and len(myString) <= ReqNum:
		temp=[myString[0]+myString[1], myString[1]+myString[0]]
		return temp
	elif len(myString) > 2:
		myString_length_temp=len(myString)
		temp_list_2=[]
		temp_list_4=[]
		while  myString_length_temp >= 1:
			#print "calling permutation(%s, %s)" %(myString[i], myString[0:i]+myString[i+1:])
			temp_list_2=permutation(myString[i], myString[0:i]+myString[i+1:])
			temppp=flatten(temp_list_2)
			temp_list_3=merge_lists(myString[i], temppp);
			temp_list_4.append(temp_list_3)
			ret_list.append(temp_list_3)
			myString_length_temp -= 1
			i += 1
		return temp_list_4

def merge_lists(x, list_b): #process [x] [abc, bcd]
        ret_list_2=[]
        for data in range(len(list_b)):
                temp_data=list_b[data] #consider each element of the list, EX:- abc
                for j in range(len(temp_data)+1):
                        if j == 0 and len(temp_data) < ReqNum:
                                ret_list_2.append(x+temp_data)
			elif j == 0 and len(temp_data) == ReqNum:
				ret_list_2.append(temp_data)
                        elif j > 0 and j <= len(temp_data) and len(temp_data) < ReqNum:
                                ret_list_2.append(temp_data[0:j]+x+temp_data[j:])
			elif j > 0 and j <= len(temp_data) and len(temp_data) == ReqNum:
				ret_list_2.append(temp_data)
        return ret_list_2

def remove_duplicate(myList):
	return list(set(myList))

final_list=permutation(my_Dummy, myString)
final_list_1=flatten(final_list)
final_list_2=remove_duplicate(final_list_1)
final_list_2.sort()
length=len(final_list_2)
print "****** Number of permutations : %d" %length
print final_list_2

