'''
r	read-only mode, file must exist
w	write-only mode, creates, or overwrites an existing file
a	write-only mode, write always appends to the end
r+	read/write mode, file must already exist
w+	read/write mode, creates, or overwrites an existing file
a+	read/write mode, write will append to end
'''

'''
    read(size) will read size characters/bytes as a string
    write(string) will write string/bytes to a file
    readline() will read a string until and including the next newline character is met
    readlines() will return a list of all lines of a file
    writelines() will write a list of lines to a file
    flush() will try to make sure that the changes made to a file are written to disk immediately
'''