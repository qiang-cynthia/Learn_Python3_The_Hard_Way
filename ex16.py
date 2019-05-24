from sys import argv

script, file_name = argv

print(f"We're going to erase {file_name}.")
print("If you don't want that, hit CTRL-C.")
print("If you want to do that, hit Enter.")

input('?')

print('Opening the file...')
target = open(file_name, 'w')

print('Truncating the file. Goodbye!')
target.truncate()

print("Now I'm going to ask you for three lines.")

line_1 = input('line 1:')
line_2 = input('line 2:')
line_3 = input('line 3:')

print("I'm going to write these to the file.")

target.write(line_1)
target.write('\n')
target.write(line_2)
target.write('\n')
target.write(line_3)
target.write('\n')

# print(target.read())

print('Finally, We close it.')
target.close()

txt = open(file_name)
print(f'Now the content inside {file_name} is:')
print(txt.read())
txt.close()
