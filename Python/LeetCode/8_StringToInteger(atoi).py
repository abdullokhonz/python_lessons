class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        sign: int = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        result: int = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        result = sign * result
        return max(min(result, 2 ** 31 - 1), -2 ** 31)
