my_dict = {'Vasya': 1985, 'Petya': 1999, 'Sveta': 2001}
print('Dict:', my_dict)
print('Existing value:', my_dict['Vasya'])
print('Not existing value:', my_dict.get('Alex'))
my_dict.update({'Roxana': 2002, 'Rex': 2000})
print('Deleted value:', my_dict.pop('Sveta'))
print('Modified dictionary:', my_dict)
# Далее работа с множествами
my_set = {1, 2, 3, 3, 2, 1, "Stol", 'stul',(2, 3, 4)}
print('Set:', my_set)
my_set.add(33)
my_set.add('golova')
my_set.remove('Stol')
print('Modified set:', my_set)