class ReverseInteger:
    def reverse(self, x: int) -> int:
        s: int = 1 if x > 0 else -1
        reversed_x: int = int(str(x * s)[::-1]) * s
        return reversed_x if -2 ** 31 <= reversed_x <= 2 ** 31 - 1 else 0
