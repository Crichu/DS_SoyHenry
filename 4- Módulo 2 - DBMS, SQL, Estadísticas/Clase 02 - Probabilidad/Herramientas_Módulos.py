class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verifica_primo(self):
        '''
        verifica los números primos de una lista de números enteros positivos.
        '''
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)
    
    def factorial(self):
        for i in self.lista:
            print(self.__factorial(i))

    def __verifica_primo(self, nro): #verifica si un número es primo o no.
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal(self, menor): #verifica el valor modal de una lista de números.
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero


def NumeroBinario(numero): #pasar un número entero a binario.

    if numero < 0 or type(numero) != int:
        print ("El número ingresado debe ser un número entero mayor a 0")
        return None
    
    elif numero == 0:
        return numero

    else:
        lista_binarios = []
        
        while numero > 0:
            parte_binaria = numero % 2 #calcula resto
            lista_binarios.append (str(parte_binaria)) # guerda el resto para armar el binario

            numero = numero // 2 # calcula la parte entera para seguir dividiendo

        lista_binarios.reverse() #reordena la lista a la inversa
        numero_binario = "".join (lista_binarios)

    return int(numero_binario)

def Fraccion_binaria (fraccion): #pasar un número decimal o fración a binario
    numero_binario = '0.'

    while fraccion > 0:
        fraccion *= 2

        if fraccion >= 1:
            numero_binario += '1' # como la variable es un str, en lugar de suma es una operación de concatenación
            fraccion -=1 

        else:
            numero_binario += '0'

    return float(numero_binario)

def numero_a_binario (numero): #combina las dos anteriores para pasar cualquier número (decimal o entero) a binario.
    parte_entera = int (numero)
    parte_decimal = numero - parte_entera

    binario_entero = NumeroBinario (parte_entera)
    binario_decimal = Fraccion_binaria (parte_decimal)

    numero_a_binario = binario_entero + binario_decimal

    return numero_a_binario

# para crear estructuras de datos: listas enlazadas
#1. Class para crear nodo
class Node:
    def __init__(self, val):
        ## Inicializamos la variable data automáticamente cada vez que llamamos a la clase Node y le asignamos un valor
        self.data = val
        ## Y por defecto le decimos que el primer siguiente al que apunta, es None
        self.next = None

    def getData(self):
        ## getData, nos devuelve el valor que almacenamos en la variable data
        return self.data

    def getNext(self):
        ## getNext, nos devuelve la información de a que valor apunta
        return self.next

    def setData(self, val):
        ## Con setData podemos asignarle un nuevo valor a nuestra variable existente
        self.data = val

    def setNext(self, val):
        ## Con setNext, podemos modificarle a que nodo apunta
        self.next = val










#2. Class para crear la lista y operar con la lista.
class LinkedList:
    def __init__(self):
        ## Iniciamos nuestra Linked List. Y lo primero que vamos a tener, va a ser un head, que no está apuntando a nada
        self.head = None

    def isEmpty(self):
        """podemos hacer es chequear si nuestra lista está vacía"""
        if (self.head == None):
            return True
        else:
            return False

    def add(self, item):
        """Añadir un item a la lista, generamos un nuevo nodo. Luego el nuevo nodo, va a ser el
           siguiente de mi head.
        """
        new_node = Node(item)
        """El nuevo nodo, se le setea al next"""
        new_node.setNext(self.head)
        """Y el head, pasa a ser el nuevo nodo"""
        self.head = new_node

    def size(self):
        """Contamos la cantidad de elementos que tenemos en la lista.
           Comenzamos en 0, y por cada iteración vamos sumando 1.
        """
        count = 0
        """Comenzamos en el head"""
        current = self.head
        """Y empezamos a contar. Mientras tengamos algo en el nodo, sumamos 1"""
        while (not(current == None)):
            count += 1 
            """Por cada iteracion vamos cambiando el puntero"""
            current = current.getNext()
            """Cuando el current es == a None, sale de la iteración
            Y devuelve la cantidad de nodos que fué encontrando."""
        return count

    def search(self, item):
        """Iterar sobre la lista para encontrar un valor. Si se encuentra dicho valor
            retorna un True, si no retorna un False."""
        current = self.head # Se define nuevamente al puntero current como el head
        found = False # y definimos a found = False, porque todavía no encontró nada
        """Entonces, vamos iterando sobre la lista, si no es None y no es False, entonces
           me cambia el found a True, que indica que lo encontramos"""
        while ((current != None) and (not found)):
            if current.getData() is item:
                found = True
            ## Una vez que lo encuentra, el current pasa al próximo
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """Se puede remover un item, es decir, un nodo.
            Le podemos decir, buscame "Google.com", y lo eliminas. 
            Si el item no se encontró en la lista, me arroja un Value Error"""
        current = self.head # comenzamos desde el head, que es el puntero. En este caso el current
        previous = None # El previous va a ser un None, porque justamente, vamos a estar empezando desde 0 con el current
        found = False # Iniciamos, el buscador con un False.
        """Mientras current NO sea None y Verdadero entonces..."""
        while((current != None) and (not found)):
            """Si el current, osea donde estamos parados, es el ítem buscao, indica que lo encontramos. 
            Cambia el valor de found a True."""
            if(current.getData() == item):
                found = True
            #Y en caso contrario, el previous, nos va guardando el anterior al que vamos recorriendo. 
            # Entonces guardo cual es el actual y le decimos, ahora saltá al siguiente.
            # Por ejemplo, si estamos en el nodo 1, el previous va a ser el nodo 1 y el current nos va a apuntar al
            # nodo 2
            else:
                previous = current
                current = current.getNext()
        if found: ## Si encuentro el valor
            if(previous == None): ## Y si a ese valor no le antecedía nada. Osea si estabamos ubicados en el primer valor
                self.head = current.getNext() # El head pasa a ser el siguiente del current
            else: # Y en el caso de que tenga algo anteriormente, le decimos que el anterior, me setee lo que le sigue
                previous.setNext(current.getNext())
        else:
            raise ValueError # Si no lo encuentra, me arroja Value not found
            print('Value not found.')

    def insert(self, position, item):
        """
        Le digo que me inserte un valor en determinada posición. 
        Como primera salvedad, si le digo que me inserte el valor en una posición que es 
        es mas larga que lo que tenemos, le digo que me arroje un error de posición.
        Que el índice está fuera del rango de nuestra lista
        ---> IndexError
        """
        if position > self.size() - 1:
            raise IndexError
            print('Index out of bounds.')
         ## En caso contrario, osea que el rango esté bien, el current comienza en el head
        current = self.head
        ## No le antecede nada (porque es el primer valor)
        previous = None
         ## Y la posición comienza en el cero
        pos = 0
        ## Si la posición es 0, básicamente sería como añadir un valor (como la función add)
        if position == 0:
            self.add(item)
        else: ## Si ocurre otra cosa, declaro un nuevo nodo
            new_node = Node(item)
            # Acá vamos corriendo hasta llegar a la posición. La posicion es la que ingresa por teclado
            # La posicion que voy corriendo como puntero está iniciada en 0. Mientras no llegue a la posición
            # voy sumando una posición
            while pos < position:
                pos += 1
                # En el previous, guardo en donde estoy "ahora" osea justo antes del nuevo current
                previous = current
                #  Ahora el current es el siguiente nodo
                current = current.getNext()
            # Una vez que se llegue al previous, que me apunte al nuevo nodo
            previous.setNext(new_node)
            # Y que el nuevo nodo, me apunte al current, osea en donde estoy ahora
            new_node.setNext(current)

    def index(self, item):
        """
        Queremos ver en que indice esta cierto valor que le preguntamos
        """
        current = self.head # comenzamos desde el head, que es el puntero. En este caso el current
        pos = 0 # Iniciamos la posición en 0 y la usamos como contador 
        found = False # Le decimos que de momento no encontró nada (porque todavía no buscó nada)
        # Mientras mi lista tenga algo y todavía no encuentre el valor
        while ((current != None) and (not found)):
            if (current.getData() == item):
                found = True
            else:
                current = current.getNext() # Devuelve la información del valor al que apunta
                pos += 1 # Sumamos 1 al contador
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position = None):
        """
        Si no se proporciona ningún argumento, devuelva y elimine el elemento
        del head. Si se proporciona la posición, devuelva y retire el artículo 
        en esa posición.
        Si el índice está fuera de los límites, retorna el IndexError
        """
        current = self.head # comenzamos desde el head, que es el puntero. En este caso el current
        if (position == None): # si no tenemos posicion
            ret = current.getData() # El ret, que es lo que estamos retornando, sería ahora el head
            self.head = current.getNext() # Y el head sería el siguiente
        else: # la posicion es mayor a nuestro tamaño de lista, que retorne un error de Indice (IndexError)
            if position > self.size():
                print('Index out of bounds')
                raise IndexError
            # Si no entra en el if de el error de rango:
            # definimos la posición en 0
            pos = 0 
            previous = None # previamente no tenemos nada
            while pos < position: # Mientras no llegue a la posción
                previous = current # voy a ir cambiando de nodo a nodo, entonces el previous va a ser donde estoy ahora
                current = current.getNext() # Y donde estoy ahora va a ser el siguiente nodo
                pos += 1 # me muevo una posición
                ret = current.getData()# Y el valor de retorno va a ser ret.
            previous.setNext(current.getNext())
        return ret

    def append(self, item):
        """Le queremos decir que añada un nuevo ítem al final de la lista"""
        current = self.head # Comienzo en el head
        previous = None # Anteriormente no tengo nada
        pos = 0 # Comienzo en el cero
        length = self.size() # Y le pasamos el tamaño para saber que tanto hay que recorrer
        while pos < length: # Mientras no llegue al final de la lista
            previous = current # guarda el valor anterior con el actual
            current = current.getNext() # El actual ahora es el próximo
            pos += 1 # Se le suma 1 a la posición
        # Entonces cuando llego al final de la lista, llego al valor length, me salgo de ese while
        new_node = Node(item) # Y lo que hago es que genere un nuevo nodo con el ítem que le pasamos al append
        if (previous == None): # Y si no teníamos nada anteriormente (osea lista vacía)
            new_node.setNext(current) # el nuevo nodo, va a apuntar en donde estoy ahora
            self.head = new_node # Y el head, va a ser el siguiente nodo
        else:
            previous.setNext(new_node)

    def printList(self):
        """Print the list"""
        current = self.head # Comenzamos nuestro puntero en el head
        while (not(current == None)): # Mientras tengamos algo, imprimimos el current
            print(current.getData())
            current = current.getNext()









### Implementación de una pila en Python (LIFO) ---> LAST IN FIRST OUT
class Estructura_Pila(object):
    def __init__(self):
        self.__list = []
    # Agregar un elemento a la Pila
    def push(self, item):
        self.__list.append(item)
        return 'Ha ingresado el elemento: ',item
    # Quitar un elemento de la Pila ... PRESTEN ATENCIÓN
    def pop(self):
        return 'Se eliminó el elemento: ',self.__list.pop()
    # Obtener el elemento superior de la Pila
    def peek(self):
        if self.__list:
            return 'El ultimo elemento de la lista es: ', self.__list[-1]
        else:
            return 'No hay nada en la lista'
    # Determinar si la Pila está vacía
    def is_empty(self):
        if self.__list == []:
            return 'La lista está vacía'
        else:
            return 'La lista tiene los siguientes elementos', self.__list
    # Devuelve el número de elementos de la lista:
    def size(self):
        longitud = len(self.__list)
        return {f'La lista contiene: {longitud} elementos'}

#if __name__ == '__main__':
#    s = Estructura_Pila()
#    s.push()









### Implementación de una cola en Python (FIFO) FIRST IN FIRST OUT
class Estructura_Cola(object):
    # Creamos lista de manera automática, cada vez que llamamos a la clase
    def __init__(self):
        self.__list = []
    # Agregamos un elemento a la cola
    def enqueue(self, item):
        self.__list.append(item)
        return {f'Se agregó a la cola el siguiente elemento: {item}'}
    # Quitar un elemento de la cola; la diferencia con el código de Pilas es que en el pop, le estamos diciendo que 
    # borre el último elemento de las lista, al no pasarle ningún número en el paréntesis, pop().
    # Mientras que en las colas ---> pop(0), se le pasa pop con el índice en 0.
    def dequeue(self):
        popeado = self.__list.pop(0)
        return {f'Se eliminó el elemento: {popeado}'}
    # Verificar si la cola está vacía
    def is_empty(self):
        if self.__list == []:
            return 'No hay nada en la cola'
        else:
            return {f'Tenemos en cola los siguientes elementos: {self.__list}'} 
    # Devolver la cantidad de elementos que tiene la cola
    def size(self):
        longitud_de_cola = len(self.__list)
        return {f'Cantidad de elementos en cola: {longitud_de_cola}'}
