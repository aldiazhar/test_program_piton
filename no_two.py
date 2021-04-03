# input string
input_string = '1+2+2'

# remove all whitespace
new_string = input_string.strip()

# initializing result
result = 0

# initializing counter
counter = -1

# initializing intCount
intCount = 0

# loop every char in var input_string
for ch in range(len(new_string)):
	# check if variable counter equals ch
    if counter == ch:
        continue
    # check if char is '-' or '+'
    if new_string[ch] in ['-', '+',]:
    	# store next char from new_string to variable next_value
        next_value = int(new_string[ch+1])
        # if char equals '-' then result - next-value
        if new_string[ch] == '-':
            result -= next_value
            counter = ch+1
        # else if char equals '+' then result - next-value
        elif new_string[ch] == '+':
            result += next_value
            counter = ch+1
    # if char is number
    else:
    	intCount +=1
    	# check if double number
    	if intCount > 1:
    		print("error")
    	else:
        	result = int(new_string[ch])
# print result
print(result)