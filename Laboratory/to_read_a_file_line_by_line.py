def file_reader(file):
    with open(file) as f:
        data = f.readlines()
        print("The content of the file line by line is:",data)


# printing the file line by line
file_reader('file.txt')

# counting the number of lines in the file
#count = 0
count_lines = len(open('file.txt').readlines())
count_words = len(open('file.txt').read())

print('The number of lines in the file are :', count_lines)
print('The number of words in the file are :', count_words, 'thus, the size of the file is', count_words, 'bytes')

# to get the file size
import os
file_size = os.path.getsize('file.txt')
print('The size of the file using OS is', file_size, 'bytes')
