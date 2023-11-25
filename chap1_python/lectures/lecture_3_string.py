s = 'Hello world'

# str classifications
s.isalnum()  # True if all characters are letters or digits
s.isalpha()  # True if all characters are letters
s.isdigit()  # True if all characters are digits
s.islower()  # True if contains letters, and all are lowercase
s.isupper()  # True if contains letters, and all are uppercase
s.isspace()  # True if all characters are whitespace
s.istitle()  # True if uppercase in the beginning of word, elsewhere lowercase


# str transformations
s.lower()  # Change all letters to lowercase
s.upper()  # Change all letters to uppercase
s.capitalize()  # Change the first character to upper case and change the rest to lower case
s.title()  # Change to titlecase
s.swapcase()  # Change all uppercase letters to lowercase, and vice versa

substr = 'll'
replacement = 'LL'
# substring
s.count(substr)  # Counts the number of occurences of a substring
s.find(substr)  # Finds index of the first occurence of a substring, or -1
s.rfind(substr)  # Finds index of the last occurence of a substring, or -1
s.index(substr)  # Like find, except ValueError is raised if not found
s.rindex(substr)  # Like rfind, except ValueError is raised if not found
s.startswith(substr)  # Returns True if string starts with a given substring
s.endswith(substr)  # Returns True if string ends with a given substring
s.replace(substr, replacement)  # Returns a string where occurences of one string are replaced by another


# trimming & adjusting
x = ''
n = 1
s.strip(x)  # Removes leading and trailing whitespace by default, or characters found in string x
s.lstrip(x)  # Same as strip but only leading characters are removed
s.rstrip(x)  # Same as strip but only trailing characters are removed
s.ljust(n)  # Left justifies string inside a field of length n
s.rjust(n)  # Right justifies string inside a field of length n
s.center(n)  # Centers string inside a field of length n






