# 1.
def factorial(n) -> int:

    if not isinstance(n, int):
        raise TypeError("El número no es un entero")
    
    if n < 0:
        raise ValueError("El número debe ser positivo o cero")
    
    def inner_factorial(n) -> int:
        if n <= 1:
            return 1
        return n * inner_factorial(n - 1)
    
    return inner_factorial(n)

# 2.

def increment(n):

    if not isinstance(n, int):
        raise TypeError("El parámetro debe un número")
    
    def inner_increment():
        return n + 1
    
    return inner_increment()

# 3.

def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power

potencia_cuadrada = generate_power(2)
potencia_cubica = generate_power(3)
potencia_novena = generate_power(9)

class generate_power():

    def __init__(self, exponent) -> None:
        self.exponent = exponent

    def power(self, base) -> int:
        return base ** self.exponent


# 4. 

def mean():
    sample = []
    def inner_mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return inner_mean

# 5.

def add_messages(func):
    def inner_add_messages():
        print("Inicio del decorador")
        func()
        print("Adios")
    return inner_add_messages

def debug(func):
    def inner_debug(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} (args: {args}, kwargs: {kwargs}) -> {result}")
        return result
    return inner_debug

@debug
def sumar(*args, **kwargs) -> int:
    temp = 0
    for arg in args:
        temp = temp + arg

    for k, v in kwargs.items():
        temp = temp + v

    return temp

if __name__ == "__main__":
    sumar(3, 5, num = 9)
    sumar(3, 5, 2, 5, num = 9)
    sumar(num1 = 9, num2 = 8)

