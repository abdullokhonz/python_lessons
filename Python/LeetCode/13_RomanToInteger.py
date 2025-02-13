class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        roman: dict = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,
        }

        total: int = 0
        prev_value: int = 0

        for char in reversed(s):
            value: int = roman[char]
            if value < prev_value: total -= value
            else: total += value
            prev_value = value

        return total


test: RomanToInteger = RomanToInteger()
print(test.romanToInt("IV"))
