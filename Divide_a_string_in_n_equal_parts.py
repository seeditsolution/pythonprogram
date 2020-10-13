# Python program to print n equal parts of string 

# Function to print n equal parts of string 
def divide_String(string, n): 
	str_size = len(string) 

	# Check if string can be divided in n equal parts 
	if str_size % n != 0: 
		print "Invalid Input: String size is not divisible by n"
		return

	# Calculate the size of parts to find the division points 
	part_size = str_size/n 
	k = 0
	for i in string: 
		if k%part_size==0: 
			print "\n", 
		print i, 
		k += 1

# Driver program to test the above function 
# Length of string is 28 
string = "a_simple_divide_string_quest"

# Print 4 equal parts of the string 
divide_String(string, 4) 
