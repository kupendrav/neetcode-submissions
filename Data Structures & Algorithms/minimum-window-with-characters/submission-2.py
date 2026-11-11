from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        min_len = float("inf")
        res = [-1, -1]

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = [left, right]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r + 1] if min_len != float("inf") else ""