class TotalCharactersInStringAfterTransformationsI:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD: int = 10 ** 9 + 7
        count: list[int] = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_count: list[int] = [0] * 26

            for i in range(25):
                new_count[i + 1] = count[i]

            new_count[0] = (new_count[0] + count[25]) % MOD
            new_count[1] = (new_count[1] + count[25]) % MOD
            count = new_count

        return sum(count) % MOD
