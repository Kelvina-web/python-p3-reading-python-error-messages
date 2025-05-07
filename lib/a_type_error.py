# Original code causing KeyError:
my_dictionary = {'a': 1, 'b': 2}
my_dictionary['c']

# Fixed code:
my_dictionary = {'a': 1, 'b': 2}
print(my_dictionary.get('c', 'Key not found'))  # or add 'c' to dictionary
