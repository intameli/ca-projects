from rpg import Character, Chest

aragorn = Character('Aragorn', 'Human')
galadriel = Character('Galadriel', 'Elf')
frodo = Character('Frodo', 'Hobbit', gold=50, items=['The One Ring'])

chest = Chest(items=['longsword', 'iron helm'], gold=25, locked=True)

print(frodo.get_obj())
print(chest.get_obj())

chest.transfer(frodo)

print(frodo.get_obj())
print(chest.get_obj())