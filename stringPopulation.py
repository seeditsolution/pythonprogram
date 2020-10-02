from collections import defaultdict
import string
def extract_popular(textstring):
    """
    Input: string
    Output: dictionary with counts for each character in a string
    """
    d = defaultdict(int)
    exclude = set(string.punctuation)
    textstring = textstring.lower()
    textstring = ''.join(ch for ch in textstring if ch not in exclude)
    for c in textstring:
        d[c] += 1
        counts = [(d[c], c) for c in d]
        counts.sort()
        counts.reverse()
    return counts
print(extract_popular("A man, a plan, a canal: Panama"))
print(extract_popular("Testing, attention please"))
