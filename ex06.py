# use f-string to format the string
types_of_people = 10
x = f'There are {types_of_people} types of people.'

binary = 'binary'
do_not = "don't"
y = f'Those who know {binary} and those who know {do_not}.'

print(x)
print(y)

print(f'I said: {x}')
print(f'I also said: "{y}"')

# use str.format function to format the string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# the combination of strings
w = 'This is the left side of...'
e = 'a string with a right side.'

print(w + e)
