numero=int(input("Número:"))
print("Divisores:")
for n in range(1,numero+1):
    if numero%n == 0:
        print(n)
