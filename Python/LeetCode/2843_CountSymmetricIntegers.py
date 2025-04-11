class CountSymmetricIntegers:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count: int = 0

        for i in range(low, high + 1):
            number: str = str(i)
            if len(number) % 2 == 1:
                continue

            length: int = len(number) // 2
            left: str = number[:length]  # Первая половина
            right: str = number[length:]  # Вторая половина

            left_sum: int = sum(int(digit) for digit in left)  # Сумма цифр левой половины
            right_sum: int = sum(int(digit) for digit in right)  # Сумма цифр правой половины

            if left_sum == right_sum:
                count += 1

        return count
