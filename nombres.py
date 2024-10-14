import sys
if len(sys.argv) < 2:
    sys.exit("Muy pocos argumentos")

for arg in sys.argv[1:]:
    print("Hola,", arg)