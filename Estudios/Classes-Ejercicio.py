class Converter():

    def __init__(self) -> None:
        self.equiv = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def int_to_roman(self, number) -> str:
        result = ""

        for x, y in self.equiv:
            #while number // x != 0:
            while number >= x:
                result += y
                number -= x
        
        return result


class RomanToInteger:

    def __init__(self):
        self.roman_to_int_map = {
          'I': 1, 'V': 5, 'X': 10, 'L': 50,
          'C': 100, 'D': 500, 'M': 1000
        }
        

    def roman_to_int(self, s):
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = self.roman_to_int_map[char]

            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value
        
        return total


class ListToSets():

    def __init__(self) -> None:
        pass

    def combinations(self, l) -> list:
        import itertools

        result = []

        for i in range(len(l) + 1):
            result.extend(list(itertools.combinations(l, i)))

        return result


class ListSum0():

    def __init__(self, l) -> None:
        import itertools

        result = []

        #for i in range(1, len(l) + 1):
        candidates = [list(x) for x in itertools.combinations(l, 3)]
        for j in range(len(candidates)):
            if sum(candidates[j]) == 0:
                result.append(candidates[j])

        self.result = result

    def __str__(self) -> str:
        return f"Los resultados son {str(self.result)}"
    


if __name__ == "__main__":
    c = ListSum0([-25, -10, -7, -3, 2, 4, 8, 10])
    print(c)