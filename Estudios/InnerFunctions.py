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

if __name__ == "__main__":
    print(generate_power(3)(2))
