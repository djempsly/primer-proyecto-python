
#Aqui es un diccionario se declara con las {}

diccionary = {
    'Yeudy': 'Mi primer hijo',
    'Ismael': 'Segundo hijo',
    'Jeff': 'Tercer hijo',
    'hijos': ['uno', 'dos', 'tres']
}

alfa = {
    'Color': 'Rubia',
    'Altura': 'Alta',
    'Tamaño' : 'Grande',
    'age': 30
}


busca = input('Escribe las palabras ')
busca = busca.lower()

print(diccionary['Yeudy'])

print(diccionary.get('Ismael'))
print(len(diccionary))

if busca in alfa:
    print('Tu nombre es Alfanelis Liberato')

diccionary['Jeff'] = 'Jeffry' #Aqui es para modificar datos en un diccionario
alfa['age'] += 4
diccionary['hijos'].append('cinco')


print(diccionary)
print(alfa)

diccionary.pop('Yeudy')
del diccionary['Jeff']
print(diccionary)
alfa['twitter'] = 'Djempsly'
print(alfa)
print(list(alfa.keys()))
print(list(alfa.values()))