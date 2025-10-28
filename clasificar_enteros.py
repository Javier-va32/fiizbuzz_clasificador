def generar_enteros():
    numeros=[]
    for i in range(1,31):
        numeros.append(i)
    return numeros

def clasificar_enteros(numeros):
    fizzbuzz = []
    fizz = []
    buzz = []
    otro = []

    for i in numeros:
        if i%3==0  and i%5==0:
            fizzbuzz.append(i)
        elif i%5==0:
            buzz.append(i)
        elif i%3==0:
            fizz.append(i)
        else:
            otro.append(i)
    return fizzbuzz, buzz, fizz, otro

def mostrar_resultados(fizzbuzz, buzz, fizz, otro):
    print(f"Los múltiplos de 3 son los números: {fizz}")
    print(f"Los múltiplos de 5 son los números: {buzz}")
    print(f"Los múltiplos tanto de 3 como de 5 son: {fizzbuzz}")
    print(f"Mientras que {otro} son números que no entran en ninguna categoría")

def main():
    numeros=generar_enteros()
    fizzbuzz, buzz, fizz, otro = clasificar_enteros(numeros)
    mostrar_resultados(fizzbuzz, buzz, fizz, otro)

if __name__=="__main__":
    main()


