class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or s is None:
            return ""

        self.start, self.max_length = 0, 1

        for center in range(len(s)):
            self.expandAroundCenter(s, center, center)
            self.expandAroundCenter(s, center, center + 1)

        return s[self.start:self.start + self.max_length]

    def expandAroundCenter(self, s: str, left: int, right: int) -> None:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            length: int = right - left + 1
            if length > self.max_length:
                self.start = left
                self.max_length = length
            left -= 1
            right += 1
