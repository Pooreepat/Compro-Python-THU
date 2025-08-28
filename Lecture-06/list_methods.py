heroes = ['Ironman','Thor','Hulk','Superman','spiderman']
h2 = ['Dr. Strange','Captain America', 'Black panther','Antman']

heroes.insert(0, h2[0])
print(heroes.index('Thor'))  
heroes.insert(heroes.index('Thor'), h2[1])
print(heroes)
heroes.remove('Superman')
heroes.append('antman')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newherose = heroes
newherose[0] = 'wonder woman'
print(heroes)
copyheros = [] + heroes
print(copyheros)
copyheros[0] = 'Hanuman'
print(heroes)
print(copyheros)