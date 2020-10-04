a=input("Enter the first word: ")
b=input("Enter the word which according to you is its anagram: ")
sorted_a=sorted(a)
sorted_b=sorted(b)
print(sorted_a)
print(sorted_b)
if sorted_a==sorted_b:
    print("The two words are the anagrams of each other.")
else:
    print("The the two words are not the anagram of each other.")
