my_name = 'wang.wzx'
my_age = 35
my_height = 175 # cm
my_weight = 60 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = "Black"

print("Let's talk about {}.".format(my_name))
print(f'He is {my_height} centimeters tall, and {my_weight} kilograms heavy.')
print("He's got {0} eyes and {1} hair.".format(my_eyes, my_hair))
print(f'His teeth are usually {my_teeth} depending on the coffee.')

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print('If I add {0}, {1}, and {2} I get {3}.'.format(my_age, my_height, my_weight, total))
