# Читаем две строки → превращаем в списки чисел с плавающей точкой
a = list(map(float, input().split()))
b = list(map(float, input().split()))

# Считаем и сразу печатаем
print(a[0]*b[0] + a[1]*b[1] + a[2]*b[2])
