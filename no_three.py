  
# initializing array list
test_list = [1, 10, 100, 200, 400, 20, 30, 900]

# variable array
numbers = []
  
# initializing k
k = 264
  
# loop variable array
count = 0
for i in test_list :
	# check if i smaller than k
    if i < k :
    	# store to varible array 
        numbers.append(i) 
  
# join all 
string_concatenating = ''.join(map(str, numbers))

# printing list 
print ("The list : " + str(test_list))

# printing the intersection 
print (string_concatenating)