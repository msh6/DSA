def recursive_vowel_consonant_counter(s, v=0, c=0):
    # Base case: When the string is empty, return the counts.
    if len(s) == 0:
        return v, c
    
    # Check if the first character is a vowel.
    if s[0] in {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}:
        v += 1
    else:
        c += 1
    
    # Recursively call with the remaining part of the string.
    return recursive_vowel_consonant_counter(s[1:], v, c)

v_count, c_count = recursive_vowel_consonant_counter("sohial")
print("Vowels:", v_count)
print("Consonants:", c_count)