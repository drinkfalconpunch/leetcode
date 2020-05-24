class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        for i, char in enumerate(s):
            found = []
            sub = ''
            for c in s[i:]:
                if c in found:
                    break
                found.append(c)
                sub += c
            if len(sub) > len(longest):
                longest = sub
        return len(longest)