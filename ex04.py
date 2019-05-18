cars = 100
space_in_car = 4
drivers = 31
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print('There are {0} cars available.'.format(cars))
print('There are only {0} drivers available.'.format(drivers))
print('There will be {0} empty cars today.'.format(cars_not_driven))
print('We can transport {} people today'.format(carpool_capacity))
print('We need to put about {:.4f} in each car.'.format(average_passengers_per_car)) # 注意最后的结果是浮点数。可以根据浮点数来判断安排是否合理
