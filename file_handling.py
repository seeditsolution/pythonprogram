#copying text of one file to another (new file).

file=open('Jain.txt')
new_file=open('new_Jain.txt','w')
print("Jain.TXT CONTENT:")
print()
for line in file:
	new_file.write(line)
	print(line)
print()
print("NEW_Jain.TXT CONTENT:")
print()
new_file=open('new_Jain.txt')
for line in new_file:
	print(line)

file.close()
new_file.close()	

#OUTPUT

# Jain.TXT CONTENT:

# hey!

# shivani here

# nice to meet you :)


# NEW_Jain.TXT CONTENT:

# hey!

# shivani here

# nice to meet you :)
