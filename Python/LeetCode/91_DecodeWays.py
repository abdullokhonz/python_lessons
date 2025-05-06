class DecodeWays:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n: int = len(s)
        dp: list[int] = [0] * (n + 1)

        dp[0]: int = 1
        dp[1]: int = 1

        for i in range(2, n + 1):
            one_digit: str = s[i - 1]
            two_digits: str = s[i - 2:i]

            if one_digit != '0':
                dp[i] += dp[i - 1]

            if 10 <= int(two_digits) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
