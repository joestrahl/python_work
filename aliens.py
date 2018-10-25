bella = {'name':'bella',
'kind of animal': 'dog',
 'owner': 'joe'
 }
     
lacy = {'name':'lacy','kind of animal': 'dog', 'owner':'maddy'}

red = {'name':'red','kind of animal':'cat', 'owner':'jim'}

animals = [bella, lacy, red]

for animal in animals:
    print(animal['name'].title() + ' is a ' + animal['kind of \
animal'] + " who is owned by " + animal['owner'].title() + ".")
