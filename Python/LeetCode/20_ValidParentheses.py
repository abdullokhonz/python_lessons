class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        mapping: dict[str: str] = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element: str = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
