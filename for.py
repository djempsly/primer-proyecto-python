# Iterando con el buble for

"""for element in range(20):
    print(element)"""

"""for element in range (1, 26):
    print(element)"""
"""
list = [24, 35, 1, 25, 52]

for element in list:
    print(element)

tupla = ('Maline', 'Kiki', 'Rodelyn')

for element in tupla:
    print(element)"""

"""product = {
    'name': 'Arroz',
    'price': 50,
    'Stock': '100'
}

for element in product:
    print(element, product[element])

for key in product:
    print(key, product[key])


for key, value in product.items():
    print(key, '===', value)

list_products= [
    {
        'name':  'Arroz',
        'price': 25
    },
    {
        'name':  'Trigo',
        'price': 20
    },
    {
        'name':  'Arroz',
        'price': 35
    },
    {
        'name':  'Arroz',
        'price': 45
    },
]

for element in list_products:
    print(element)"""

 #Ciclo Anidado

my_list = [1, -2, 3, -5, -7, 9, 8]
new_list = []

for i in my_list:
    if i > 0:
        new_list.append(i)
        print(new_list)