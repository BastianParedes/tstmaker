def funcion_decoradora(funcion):
    def wrapper(*args, **kwargs):
        print("inicio")
        resultado = funcion(*args, **kwargs)
        print("final")
        return resultado
    return wrapper

# @funcion_decoradora      esto hace la decoración y es exactamente lo mismo que hacer la igualdad de abajo         suma = funcion_decoradora(suma)
def suma(a,b):
    resultado = 1+2
    print(resultado)
    return resultado


suma = funcion_decoradora(suma)
suma(1,2)

