# Valor flotante en pytohn

x = 3.3
print (x)

y = 1.1 + 2.2
print(y)

print(x == y)

# El resultado sería false, ya que hay una gran direfencia entre los dos valores ( 3.3 para X, 3.3000000000000000003 para Y)

# Usando Format se puede reducir la cantidad de decimal

y_str = format(y, '.2g')
print(y_str)

print(x == y_str)
print(y_str == str(x))

# ahora vamos a ahacer una tolerance

tolerance = 0.00001

print(abs(x - y) <tolerance)








