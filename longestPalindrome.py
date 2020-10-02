def longestPalindrome(text):
    '''Prints the longest Palendrome substring from text'''
    palstring = set()  #ensures that similar pattern is stored only once
    longest = 0
    for i in range(len(text)-1):
        for j in range(i+2,len(text)+1):
            pattern = text[i:j]  #generates words of min lenght 2 (substring)
            if pattern == pattern[::-1]:  #checks for palendrome
                palstring.add(pattern)   #stores all palindrome
                if len(pattern) > longest:
                    longest = len(pattern)

    if len(palstring) == 0:
        print("No palindrome substring found found")
    else:
        print("Longest palindrome string are ")
        for pattern in palstring:
            if len(pattern) == longest:
                print(pattern)

longestPalindrome(input("Enter some text : "))
