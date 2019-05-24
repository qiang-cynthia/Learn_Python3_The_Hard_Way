from sys import argv

a = input('The first variable: ')
b = input('The second variable: ')

script, a, b = argv

print('The script is called: ', script)
print('The first variable is: ', a)
print('The second variable is :', b)
