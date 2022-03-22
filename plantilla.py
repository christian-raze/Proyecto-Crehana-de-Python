#Las preguntas que te irá haciendo la esfinge corresponden a los print de esta plantilla
#Por favor completa cada reto

#Clase 1 Proyecto: Definidendo la aventura

#Reto 1 - Pon tu respuesta después del print
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

cantimplora = 10.5
litro_de_agua = 5
telescopio = 55
brujula = 20
ropa_especial = 75
espada_aventurera = 200
sandalias_especiales = 45
mapa = 45
flauta = 15
libreta = 2
libro_informativo = 16
linterna_funcional = 30
snacks = 1
botas = 50

#Reto 2 - Pon tu respuesta después de cada print
print("Lista tres objetos del equipamiento: Nombre y valor")

#Respuesta
print("cantimplora", cantimplora)
print("ropa_especial", ropa_especial)
print("mapa", mapa)

print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

#Respuesta
cantimplora_llena = litro_de_agua + litro_de_agua/2

print("¿El precio del agua en botella es menor al de la linterna funcional?")

#Respuesta
if cantimplora_llena > linterna_funcional:
    print("El precio de la catimplora llena es mayor que la linterna funcional")
else:
    print("no lo es 😌")

print("¿Cuanto valdría comprar unos snacks y una brujula?")

#Respuesta
print(snacks + brujula) 

print("¿Si tienes 100 puntos, te alcanza para comprar unas botas?")

#Respuesta
if botas < 100:
    print("Sí me alcanza")
else:
    print("no me alcanza 😪")

#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("La esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")

mis_objetos = cantimplora_llena + libro_informativo + brujula + ropa_especial + sandalias_especiales
mis_objetos_str = ["cantimplora_llena", "libro_informativo", "brujula", "ropa_especial", "sandalias_especiales"]

if mis_objetos < 200:
    print("Muy bien, puedes llevar estos 5 objetos")
else:
    mis_objetos -= ropa_especial
    if mis_objetos < 200:
        print("Quitaste un objeto para no pasar el límite")
    else:
        print("quita un elemento más y estamos listos")
        mis_objetos -= brujula

if mis_objetos < 200:
    print("Estamos listos!! 😁")
    print("Estas llevando " + str(mis_objetos) + " trekjuls")
    print("Los objetos son: " + str(mis_objetos_str))




#Reto 4 - Pon tu respuesta después del print
print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")
#Respuesta
mochila_dos = 0

while mochila_dos < 200:
    mochila_dos += cantimplora_llena 
    print("La mochila dos tiene: ", mochila_dos)

mochila_dos -= cantimplora_llena
print("Quita una catimplora")



#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")

mochila_actualizada = {
    "cantimplora_llena" : {"cantidad": 1, "valor_unitario": cantimplora_llena},
    "libro_informativo" : {"cantidad": 1, "valor_unitario": libro_informativo},
    "brujula" : {"cantidad": 1, "valor_unitario": brujula},
    "ropa_especial" : {"cantidad":1, "valor unitario": ropa_especial},
    "sandalias_especiales" : {"cantidad": 1, "valor_unitario": sandalias_especiales}
}

mochila_dos_actualizada = {
    "cantimplora_llena" : {"cantidad": 26, "valor_unitario": cantimplora_llena}
}


#Reto 5 - Pon tu respuesta después del print
print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")

vehiculo = [{}] * 8

for compartimiento in range(8):
    vehiculo[compartimiento] = {
        "cantimplora_llena" : {"cantidad": 1, "valor_unitario": cantimplora_llena},
        "libro_informativo" : {"cantidad": 1, "valor_unitario": libro_informativo},
        "brujula" : {"cantidad": 1, "valor_unitario": brujula},
        "ropa_especial" : {"cantidad":1, "valor unitario": ropa_especial},
        "sandalias_especiales" : {"cantidad": 1, "valor_unitario": sandalias_especiales}
    }
    print("Acabas de armar la mochila para el compartimiento: ", compartimiento + 1)


for mochila in vehiculo:
    print(mochila)



#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")

def agregarElementosAMochilas():
    for mochila in range(4):
        vehiculo[mochila] = {
            "cantimplora_llena" : {"cantidad": 1, "valor_unitario": cantimplora_llena},
            "linterna_funcional" : {"cantidad": 1, "valor_unitario": linterna_funcional},
            "brujula" : {"cantidad": 9, "valor_unitario": brujula},
        }
    imprimir(vehiculo)
    calcularTotalElementosEnMochilas(vehiculo)

def calcularTotalElementosEnMochilas(vehiculo):
    total_elementos_mochilas = {}
    
    print("Calculando elementos en mochila")
    for mochila in vehiculo: 
        for elemento, detalle in mochila.items(): 
            if elemento in total_elementos_mochilas:
                total_elementos_mochilas[elemento] += detalle["cantidad"]
            else:
                total_elementos_mochilas[elemento] = detalle["cantidad"]

    print(total_elementos_mochilas)


def imprimir(estructura):
    for objeto in estructura:
        print(objeto)

agregarElementosAMochilas()

