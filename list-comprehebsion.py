# List Comprehension

quadrados = [x ** 2 for x in range(6)]

print(quadrados)

pares = [x for x in range(6) if x % 2 == 0]

print(pares)

impares = [x for x in range(10) if x % 2 == 1]
print(impares)
