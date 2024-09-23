def length_of_longest_substring(s: str) -> int:
    char_set = set()  # Set to store unique characters in the window
    start = 0         # Left pointer of the window
    max_len = 0       # To store the maximum length of substring found
    for end in range(len(s)):
        while s[end] in char_set:  # If we find a duplicate, shrink the window
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])  # Add the new character to the set
        max_len = max(max_len, end - start + 1)  # Update max length if needed
    return max_len

# Test cases
print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))     
print(length_of_longest_substring("pwwkew"))    
print(length_of_longest_substring("abcdefgh"))  
print(length_of_longest_substring("a"))         
