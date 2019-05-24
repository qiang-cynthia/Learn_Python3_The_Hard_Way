# Reading file with input
file_name = input('The file ready to read is: ')

file_content = open(file_name)
print(f'What inside the {file_name} is:')
print(file_content.read())
file_content.close()
