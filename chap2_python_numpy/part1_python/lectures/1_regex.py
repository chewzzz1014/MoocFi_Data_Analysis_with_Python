# basics
import re

re.match(r"[A-Za-z_][A-Za-z_0-9]*\Z", str) # to test whether a string is a valid variable name

# some common regex notations
'''
. Matches any character
[...] Matches any character contained within the brackets
[^...] Matches any character not appearing after the hat (ˆ)
ˆ Matches the start of the string
$ Matches the end of the string
* Matches zero or more previous RE
+ Matches one or more previous RE
{m,n} Matches m to n occurences of previous RE
? Matches zero or one occurences of previous RE
'''

'''
`\d` same as `[0-9]`, matches a digit
`\D` same as `[ˆ0-9]`, matches anything but a digit
`\s` matches a whitespace character (space, newline, tab, ... )
`\S` matches a nonwhitespace character
`\w` same as `[a-zA-Z0-9_]`, matches one alphanumeric character
`\W` matches one non-alphanumeric character
'''

re.search(r'\bback\b', s)
re.findall(r'\w+ing\b', s)


'''
    re.match(pattern, str)
    re.search(pattern, str)
    re.findall(pattern, str)
    re.finditer(pattern, str)
    re.sub(pattern, replacement, str, count=0)
'''
