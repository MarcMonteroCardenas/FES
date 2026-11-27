###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio} {nom}")

saludar_a("Marc")
saludar_a("Marc", "Genial")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(num):
    if num%2 == 0:
        return True
    else:
        return False

es_parell(4)
es_parell(5)

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(numeros):
    suma = 0
    i = 0
    for idx in numeros:
        suma += idx
        i += 1 
    return suma / i   
llista = [2,5,6,8,5,7]
mitjana(llista)

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
sumar_tot(2,5,9,3,10,30)

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().

def taula_multiplicar(numero, limit = 10):
    for i in range(0,limit):
        print (f"{numero * i + 5}")

taula_multiplicar(5)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print (f"{clau}: {valor}")
mostrar_perfil(nom = "marc", valor = "string", grau = "enginyeria en telecos")


# Exercici 7: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.

def comptar_vocals(text):
    vocals = "aeiou"
    cont = 0
    for lletra in text:
        if lletra in vocals:
            cont += 1
    return cont

comptar_vocals("hola")
        
# Exercici 8: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.

def minim_i_maxim (numeros):
    i = 0
    valor_max = numeros[0]
    valor_min = numeros[0]
    for valor in numeros:
        if valor > valor_max:
            valor_max = valor
        if valor < valor_min:
            valor_min = valor
    return valor_max, valor_min

maxim, minim = minim_i_maxim([1,5,8,10,5])
print(f"Valor max: {maxim}, Valor min: {minim}")

# Exercici 9: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.

def es_palindrom(text):
    confirmacio=text[::-1].lower() 
    if confirmacio == text:
        return True
    else:
        return False

es_palindrom("hola")
es_palindrom("abbbba")