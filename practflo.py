a = 7.6
print(a)

y = 3.2 + 4.4
print(y)


print (a == y)

y_str2 = format(y, '.2g')
print (y_str2)

print(y_str2 == str(a))

tolerance = 0.00001

print(abs(a-y) <tolerance)


