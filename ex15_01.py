# Reading file with argv
from sys import argv

script, file_name = argv

file_content = open(file_name)
print(f'What inside the {file_name} is:')
print(file_content.read())
file_content.close()
