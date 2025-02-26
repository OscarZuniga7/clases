def main():
    nombre = input("Cuál es tu nombre? ")
    print(hello(nombre))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()