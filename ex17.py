from sys import argv

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}.')

read_file = open(from_file)
file_content = read_file.read()

print(f'The input file is {len(file_content)} bytes long.')

write_file = open(to_file, 'w')
write_file.write(file_content)

print('Alright, all done.')

read_file.close()
write_file.close()

check_file = open(to_file)
print('Now, after copying, the content of the target_file is:')
print(check_file.read())

check_file.close()


open(to_file, 'w').write('Some things need to be copied below:')
