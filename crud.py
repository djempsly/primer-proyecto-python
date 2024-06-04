#CRUD, Create, Read, Update and Delete
#Estos metodos vamos a aprender ahora

numbers = [2, 1, 3, 4, 5, 8, 9]
letter = ['a', 'd', 'c', 'h', 'b', 'e', 'f']

print(numbers)
numbers.append(20)

print( numbers)
print(numbers[2:5 -1])

numbers[-1] = 50

print(numbers)

#El métdo insert recibe dos parametros
numbers.insert(2, 0)
print(numbers)

junto = numbers + letter

print(junto)

# EL metodo index sirve para preguntar por una posicion especifico de un elemento

index = junto.index('a')

junto[index] = 'z'

print(junto)

index1 = numbers.index(4)
numbers[index1] = 8

print(numbers)


junto.remove('z')
print(junto)
numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

letter.sort()
print(letter)

letter.reverse()
print(letter)

