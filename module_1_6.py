my_dict = {'Denis': 1990, 'Kirill': 1993, 'Alexey': 1995}
print(my_dict)
print(my_dict.get('Denis'))
print(my_dict.get('Anton'))
my_dict.update({'Igor': 1985, 'Sergey': 2000})
ex = my_dict.pop('Kirill')
print(ex)
print(my_dict)
my_set = {1, 2, 3, 3, 2, 1, 'Denis', 'Anton', 'Denis', 32.4, 33.1, 32.4}
print(my_set)
my_set.add(1000000000)
my_set.add(2222)
my_set.remove('Denis')
print(my_set)
