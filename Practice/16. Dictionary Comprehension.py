names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print("Zip object:", list(zip(names, heroes)))
# I want a dict{'name': 'hero'} for each name and hero in names and heroes list

# Normal way
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print("Normal way:", my_dict, sep='\n', end='\n\n')

# Using Dictionary Comprehension
my_dict_comp = {name: hero for name, hero in zip(names, heroes)}
print("Using Dictionary Comprehension:", my_dict_comp, sep='\n', end='\n\n')

# If I want to change names to uppercase in the dict
my_dict_comp_upper = {name.upper(): hero for name, hero in zip(names, heroes)}
print("Using Dictionary Comprehension with UPPERCASE names:", my_dict_comp_upper, sep='\n', end='\n\n')

# If I want to change names to uppercase in the dict only if the name has more than 4 letters
my_dict_comp_conditional = {name.upper(): hero for name, hero in zip(names, heroes) if len(name) > 4}
print("Using Dictionary Comprehension with UPPERCASE names (len>4):", my_dict_comp_conditional, sep='\n', end='\n\n')

