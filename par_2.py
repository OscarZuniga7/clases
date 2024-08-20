

def main():
    x = int(input("¿Qué es x? "))
    if es_par(x):
        print("es número Par")
    else:
        print("Impar")


def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
