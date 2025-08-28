heroes = ['Ironman', 'Thor', 'Hulk','spiderman']
print(heroes)

print('Please Select Menu')
print('1. Display Heroes')
print('2. Add Hero')
print('3. Insert Heroes')
print('4. Remove Hero')
print('5. Display Sorted Heroes(Ascending/Descending)')

choice = int(input('Enter your choice: '))
if choice == 1:
    print('Heroes:', heroes)
elif choice == 2:
    new_hero = input('Enter the name of the hero to add: ')
    heroes.append(new_hero)
    print('Updated Heroes:', heroes)
elif choice == 3:
    new_hero = input('Enter the name of the hero to insert: ')
    position = int(input('Enter the position to insert the hero (0 for start): '))
    heroes.insert(position, new_hero)
    print('Updated Heroes:', heroes)
elif choice == 4:
    hero_to_remove = input('Enter the name of the hero to remove: ')
    if hero_to_remove in heroes:
        heroes.remove(hero_to_remove)
        print('Updated Heroes:', heroes)
    else:
        print(f'Hero "{hero_to_remove}" not found in the list.')
elif choice == 5:
    sort_order = input('Enter "asc" for ascending or "desc" for descending order: ')
    if sort_order.lower() == 'asc':
        heroes.sort()
    elif sort_order.lower() == 'desc':
        heroes.sort(reverse=True)
    else:
        print('Invalid sort order. Displaying unsorted heroes.')
    print('Sorted Heroes:', heroes)
