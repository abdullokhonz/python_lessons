class LengthOfLastWord:
    def lengthOfLastWord(self, s: str) -> int:
        arr: list[str] = list(map(str, s.split()))

        result: int = len(arr[len(arr) - 1])

        return result
