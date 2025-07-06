import random
import time   
#Damos la bienvenida 
print("Bienvenido a quien quiere ser millonario $$")
nombre = input("ingresa tu nombre jugador: ")
dinero = 0
print("tu dinero inicial es: ",dinero)
print("cada vez que contestes una pregunta correcta ganaras 100.000 pesos")
print("vamos a empezar a jugar en 5 segundos preparate ",nombre)
#vamos a declarar una variable que vas a ser los comodines por separado en un diccinario
comodines = {
    "eliminar" : False,
    "llamar" : False,
    "cambiar" : False
}
time.sleep(5)
#ahora vamos a crear un dicionario y dntro llevaros los niveles por lista y dentro otro diccionario llevando las preguntas
preguntas = {
    1: [
        {"pregunta" : "¿cual es la capital de españa?",
         "opciones" : ["a.madrid", "b.barcelona", "c.valencia", "d.sevilla"],
         "respuesta" : "a"},
        {"pregunta" : "cuantos dias tiene un año comun?",
         "opciones" : ["a.365","b.366","c.360", "d.380"],
         "respuesta" : "a"}
    ],
    2: [
        {"pregunta" : "¿¿Qué planeta es conocido como el planeta rojo?",
         "opciones" : ["a. marte", "b.venus", "c. Júpiter", "d. Saturno"],
        "respuesta" : "a"},
        {"pregunta" : "¿Qué instrumento se toca con un arco?",
        "opciones" : ["a. piano", "b. gitarra", "c. Violín", "d. Flauta"],
        "respuesta" : "c" }
    ],
    3: [
        {"pregunta" : "¿Quién escribió Don Quijote de la Mancha?",
         "opciones" : ["a. Gabriel García Márquez", "b. Pablo Neruda", "c. Miguel de Cervantes", "d. Juan Rulfo"],
         "respuesta" : "c"},
        {"pregunta" : "¿Qué océano es el más grande?",
         "opciones" : ["a. Índico", "b. Atlántico", "c. Pacífico", "d. Ártico"],
         "respuesta" : "c"}
    ],
    4: [
        {"pregunta" : "¿Qué evento ocurrió en 1492?",
         "opciones" : ["a. Fin de la 1ra Guerra Mundial", "b. Revolución Francesa", "c. Descubrimiento de América", "d. Guerra Civil Española"],
        "respuesta" : "c"},
        {"pregunta" : "¿Qué escritor colombiano ganó el Nobel?",
        "opciones" : ["a. Vargas Llosa", "b. García Márquez", "c. Cortázar", "d. Borges"],
        "respuesta" : "b" }
    ],
    5: [
        {"pregunta" : "¿País conocido por la Torre Eiffel?",
         "opciones" : ["a. Italia", "b. Francia", "c. Alemania", "d. España"],
         "respuesta" : "b"},
        {"pregunta" : "¿Qué gas es esencial para respirar?",
         "opciones" : ["a. Nitrógeno", "b. Oxígeno", "c. Dióxido de carbono", "d. Helio"],
         "respuesta" : "b"}
    ],
    6: [
        {"pregunta" : "Capital de Argentina?",
         "opciones" : ["a. Lima", "b. Montevideo", "c. Santiago", "d. Buenos Aires"],
        "respuesta" : "d"},
        {"pregunta" : "¿Qué país tiene forma de bota?",
        "opciones" : ["a. Portugal", "b. Italia", "c. Grecia", "d. Turquía"],
        "respuesta" : "b" }
    ],
    7: [
        {"pregunta" : "¿Qué famosa novela fue escrita por Jane Austen?",
         "opciones" : ["a. Orgullo y prejuicio", "b. 1984", "c. Cien años de soledad", "d. Crimen y castigo"],
         "respuesta" : "a"},
        {"pregunta" : "¿Qué es el Renacimiento?",
         "opciones" : ["a. Una guerra", "b. Un periodo cultural", "c. Una religión", "d. Una ciudad"],
         "respuesta" : "b"}
    ],
    8: [
        {"pregunta" : "¿Quién formuló la teoría de la relatividad?",
         "opciones" : ["a. Newton", "b. Einstein", "c. Galileo", "d. Tesla"],
        "respuesta" : "b"},
        {"pregunta" : "¿Capital de Japón?",
        "opciones" : ["a. Kioto", "b. Osaka", "c. Tokio", "d. Hiroshima"],
        "respuesta" : "c"}
    ],
    9: [
        {"pregunta" : "¿Año en que cayó el muro de Berlín?",
         "opciones" : ["a. 1989", "b. 1991", "c. 1975", "d. 2000"],
         "respuesta" : "a"},
        {"pregunta" : "¿Año de fundación de la ONU?",
         "opciones" : ["a. 1945", "b. 1939", "c. 1919", "d. 1960"],
         "respuesta" : "a"}
    ],
    10: [
        {"pregunta" : "¿Capital de Mongolia?",
         "opciones" : ["a. Ulan Bator", "b. Astana", "c. Bishkek", "d. Kabul"],
        "respuesta" : "a"},
        {"pregunta" : "¿Poeta chileno Premio Nobel 1971?",
        "opciones" : ["a. Neruda", "b. Mistral", "c. Huidobro", "d. Vargas Llosa"],
        "respuesta" : "a" }
    ],
}

#en este bucle podemos extraer una pregunta una opcion y una respuesta cmo gracias al bucle k va pasando y
#  volviendo a pasarpor cada pregunta eso si siempre se va a escoger la primera pregunta 

for nivel in range(1,11): 
    print("\n nivel", nivel)

    pregunta = preguntas[nivel][0]
    segunda = preguntas[nivel][1]
    opciones = pregunta ["opciones"]
    correcta = pregunta ["respuesta"]
    time.sleep(2)
    #ejecutamos el while siempre y se rompe con un break k esta alfin si la respuesta es correcta 
    # osea si esta en true solo se puede romper con un break o con un exit
    #--despues con este print imprime el mismo bucle k tiene pregunta una vez y imprime la pregunta 
    while True:
        print("\n", pregunta["pregunta"])
        #con este recorremos las opciones una por una tambien como si fue el nivel 1
        for op in opciones:
            print(op)
        #con estos falses comrpobamos si ya se ha usado si ya se uso tuvo k haberse puesto true en el momento k 
        # lo utilizamos eso lo hace l variable de abajo
        if comodines ["eliminar"] == False:
            print("\n**escribe '1' para usar tu primero comodin quitar dos opciones incorretas\n---------------------------------------------")
        if comodines ["llamar"] == False:
            print("**esribe '2' para usar su segundo comodin y llamar un amigo que te de una sugerencia\n---------------------------------------------")
        if comodines ["cambiar"] == False:
            print("**esribe '3' para usar tu tercer comodin y cambiar la pregunta del mismo nivel\n---------------------------------------------")
        #esto lo k hace es limpiar el comentario con el strip eliminando los espacios y con el lower lo convierte a minusculas
        respuesta = input ("\ntu respuesta: ").strip().lower()
        #esto lo k hace es verificar k el usuario halla escrito exactamente uno y verifica tambien si ya se ha usdo si no no lo corre
        if respuesta == "1" and comodines["eliminar"] == False:
            #con esto vamos  acrear una lista en una var
            incorrectas = []
            #el op recorre todas las opciones de opciones segun el bucle en k valla y  # ojo k abajo compara con la primera 
            # letra  de identificacion  osea abcd y   si es diferente a correcta todas las restantes las va a meter en la lista
            #  de incorrectas despues en una var con el random elige dos incorrectas y las imprime segun el orden de iteracion
            for op in opciones:
                if op[0] != correcta:
                    incorrectas.append(op)
            eliminadas = random.sample(incorrectas,2)
            print("se eliminaron:", eliminadas[0], "y",eliminadas[1])
            #rcorre cada opcion ya sabiendo k op esta iterado con 0 osea la posicion 0 recorre opciones y verifica si 
            #no esta en eliminadas entonces agregar a la lista nuevas opciones la op k son las opciones restantes y por 
            # ultimo comodines se convierte en true despues de haber utilizado su ciclo
            nuevas_opciones = []
            for op in opciones:
                if op not in eliminadas:
                    nuevas_opciones.append(op) 
            opciones = nuevas_opciones
            comodines["eliminar"] = True 
#con este estamos llamando el amigo el cual verificamos si es false si si crea una variable donde usamos el 
# random para elegir algunas de las opciones donde despues se imprime y vuelve el comodin verdadero y k no se pueda volver a activar 
        elif respuesta == "2" and comodines ["llamar"] == False:
            ayuda = random.choice(opciones)
            print("tu amigo te suguiere la siguiente respuesta: ", ayuda)
            comodines["llamar"] = True 

        elif respuesta == "3" and comodines ["cambiar"] == False:
            pregunta = segunda
            opciones = pregunta ["opciones"]
            correcta = pregunta["respuesta"]
            comodines["cambiar"] = True 
            print("pregunta cambiada.")
            
        elif respuesta in ["a","b","c","d"]:
            if respuesta == correcta:
                print( " muy bien correcto")
                dinero += 100000
                print("ganaste una cantidad de: ",dinero)
                break
            else:
                print("incorrecto. esa no es la opcion m,correcta era", correcta.upper)
                print("""Has perdido lo sentimos...\ndinero final: """, dinero)
                exit()
        else:
            print("por favor escribe una opcion valida")


print("\n felicidades ",nombre)
print("\n has ganado un total de: ", dinero)  
