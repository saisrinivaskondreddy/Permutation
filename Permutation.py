#!/usr/bin/python

first_input=raw_input("")
myString=[]
myString, myNum=first_input.split(" ")
ret_list=[]
my_Dummy='a'

def factorial(n):
    #while i > 0:
    #    n = n * n-1
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        n = n * factorial(n-1)
    return n

def permutation(a, myString):  #  a - dummy in case of first call , b - n distinct objects taken r at a time 
	i=0
	#print ("DEBUG : in-side function permutations %d times" %i)
	#print "my string.. recursion : %s" %myString
	temp_list_2=[]
	if len(myString) == 2:
		#print "DEBUG : in-side function permutations - String Length 2"
		temp=[myString[0]+myString[1], myString[1]+myString[0]]
		return temp
	elif len(myString) == 3:
		#print "DEBUG : in-side function permutations - String Length 3"
		temp=[myString[0]+myString[1]+myString[2], myString[0]+myString[2]+myString[1], myString[1]+myString[0]+myString[2], myString[1]+myString[2]+myString[0], myString[2]+myString[1]+myString[0], myString[2]+myString[0]+myString[1] ]
		return temp
	elif len(myString) > 3:
			#print ("DEBUG : in-side function permutations - String Length MORE %d " % len(myString))
			myString_length_temp=len(myString)
			temp_list_2=[]
		#while  myString_length_temp >= 1:
			#print ("will call permutation of %c, %s" %(myString[i] myString[0:i]+myString[i+1:]) )
			#print ("will call permutation of %c with" %myString[i])
			#print ("will call permutation of %s" %myString[0:i])
			#print ("will call permutation of %s" %myString[i+1:])
			#print ("will call permutation of %s" %(myString[0:i]+myString[i+1:]) )
			temp_list_2=permutation(myString[i], myString[0:i]+myString[i+1:])
			temp_list_3=merge_lists(myString[i], temp_list_2);
			#print "Going to print temp_list_3 *****************"
			#print temp_list_3
			#print "Going to print temp_list_3 *****************"
			ret_list.append(temp_list_3)
			#ret_list.append(permutation(myString[i], myString[0:i]+myString[i:]))
			myString_length_temp -= 1
			i += 1
			return temp_list_3
	#return temp_list_3

def merge_lists(x, list_b): #process [x] [abc, bcd]
        ret_list_2=[]
        for data in range(len(list_b)):
                temp_data=list_b[data] #consider each element of the list, EX:- abc
		#print "data lenthh : %d" % len(temp_data)
                for j in range(len(temp_data)+1):
                        if j == 0:
				#print ("j is : %d" %j)
				#print (x+temp_data)
                                ret_list_2.append(x+temp_data)
                        elif j > 0 and j <= len(temp_data):
				 #print ("j is : %d" %j)
				 #print (temp_data[0:j]+x+temp_data[j:])
                                 ret_list_2.append(temp_data[0:j]+x+temp_data[j:])
#		print "======="
        return ret_list_2

def remove_duplicate(myList):
	return list(set(myList))

#comb( myString );
#lst_input = ['xyz', 'tuv']
#final_list=merge_lists('a', ['xyz', 'tuv']);
final_list=permutation(my_Dummy, myString)
final_list_1=remove_duplicate(final_list)
final_list_1.sort()
length=len(final_list_1)
print "****** Number of permutations : %d" %length
print final_list_1

