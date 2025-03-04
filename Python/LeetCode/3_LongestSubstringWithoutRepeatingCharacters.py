class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_length = 0, 0
        window: set[str] = set()

        for end in range(len(s)):
            current_char: str = s[end]

            while current_char in window:
                window.remove(s[start])
                start += 1

            window.add(current_char)

            max_length = max(max_length, end - start + 1)

        return max_length
