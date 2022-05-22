from math import trunc


acu = 0
acu1 = 0
acu2 = 0
acu3 = 0
acu4 = 0
acu5 = 0
acu6 = 0
sum = 0
unidades = int
decenas = int
centenas = int


lista_numeros = [i for i in range(2023)]
# print(list(lista_numeros))
filtrar_pares = lambda x: x % 2 == 0
pares = filter(filtrar_pares, lista_numeros)

for i in pares:
    print((i))

    if i > 1 and i < 2023:
        unidades = i % 10
        i = trunc(i / 10)
        decenas = i % 10

        i = trunc(i / 10)
        centenas = trunc(i % 10)

        i = trunc(i / 10)
        unidad_mil = i

        if (
            centenas != 0
            and (
                unidades == 0
                or unidades == 2
                or unidades == 4
                or unidades == 6
                or unidades == 8
            )
            and decenas == 1
            and unidad_mil == 0
        ):
            acu = acu + 1
            # caso 2 solo cuenta para dos digitos
        if (
            decenas == 1
            and (
                unidades == 0
                or unidades == 2
                or unidades == 4
                or unidades == 6
                or unidades == 8
            )
            and centenas == 0
            and unidad_mil == 0
        ):
            acu1 = acu1 + 1
        # caso 1 solo cuenta para tres digitos fijando decenas a 1

        if (
            centenas == 1
            and (
                unidades == 0
                or unidades == 2
                or unidades == 4
                or unidades == 6
                or unidades == 8
            )
            and unidad_mil == 0
        ):
            acu3 = acu3 + 1
        # caso 3 solo cuenta tres digitos fijando centenas a 1
        if (
            unidad_mil == 1
            and (
                unidades == 0
                or unidades == 2
                or unidades == 4
                or unidades == 6
                or unidades == 8
            )
            and centenas != 1
            and decenas != 1
        ):
            acu4 = acu4 + 1
        # caso 6
        if (
            unidad_mil == 1
            and (
                unidades == 0
                or unidades == 2
                or unidades == 4
                or unidades == 6
                or unidades == 8
            )
            and centenas == 1
            and decenas != 1
        ):
            acu5 = acu5 + 1
        if (
            unidad_mil == 1
            and (
                unidades == 0
                or unidades == 2
                or unidades == 4
                or unidades == 6
                or unidades == 8
            )
            and centenas == 1
            and decenas == 1
        ):
            acu6 = acu6 + 1
        # caso 5
        if (
            unidad_mil == 2
            and (
                unidades == 0
                or unidades == 2
                or unidades == 4
                or unidades == 6
                or unidades == 8
            )
            and (centenas == 0)
            and decenas == 1
        ):
            acu2 = acu2 + 1
print("unidad 0")
print("decenas", acu1)
print("centenas", acu + acu3)
print("unidad de mil", acu4 + acu2 + acu5 + acu6)
print(
    "Total de veces que se escribio el uno es",
    acu + acu1 + acu2 + acu3 + acu4 + acu5 + acu6,
)
