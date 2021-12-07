import re


def validPalindrome(s):
    s = s.lower()
    s = re.sub('[\W_]+', '', s)
    if len(s) % 2 != 0:
        s = s.replace(s[len(s)//2],"")
    return s[:len(s)//2] == (s[len(s)//2:])[::-1]





    






print(validPalindrome('a man, a plan, a canal: Panama'))