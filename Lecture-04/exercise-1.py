print('--------------------------')
print('KPH\tMPH')
print('--------------------------')

for kph in range(60,131,10):
    mph = kph * 0.6214
    print(kph,'\t',format(mph,'.1f'))



