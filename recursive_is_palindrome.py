def recursive_is_palindrome(s):
    # Base case: if string empty or contains only one character
    if len(s) <= 1:
        return True
    
    # Comparing the first and last element
    if s[0] != s[-1]:
        return False
    
    # Recursively check the substring without the first and last characters.
    return recursive_is_palindrome(s[1:-1])

print(recursive_is_palindrome("sohail"))


def vowel_consonant(s, v=0, c=0):
    #base case
    if len(s) == 0:
        return v, c
    
    if s[0] in {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}:
        v += 1
    else:
        c += 1
        
    return vowel_consonant(s[1:], v, c)

print(vowel_consonant("sohial"))

    