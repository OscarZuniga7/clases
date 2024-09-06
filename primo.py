n = int(input("Ingresa número entero: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} no es número primo")
        break
    else:
        print(f"{n} es número primo")
        break


    
