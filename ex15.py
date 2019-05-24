from sys import argv

# Reading file with argv
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())
txt.close()

# Reading file with input
print('Type your filename again: ')
file_again = input('> ')

txt_again = open(file_again)

print(f"Here's your file {file_again}: ")
print(txt_again.read())
txt_again.close()
