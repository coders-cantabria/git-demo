# Enumerando los números naturales por debajo de 10 que son múltiplos de 3 o 5,
# obtenemos 3, 5, 6 y 9. La suma de éstos es 23.
#
# Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000.
#
# Fuente: https://projecteuler.net/problem=1


def multiplo_tres(n):
    if n % 3 == 0:
        return True
    else:
        False


def multiplo_cinco(n):
    if n % 5 == 0:
        return True
    else:
        False


def main():
    sum = 0
    i = 0
    while i < 10:
        if multiplo_tres(i) or multiplo_cinco(i):
            sum += i
        i += 1
    print('The sum is %d' % sum)


if '__main__' == __name__:
    main()
