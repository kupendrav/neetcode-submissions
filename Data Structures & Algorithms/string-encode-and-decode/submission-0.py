from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Build encoded string by concatenating <length>#<string> for each string
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the separator #
            j = i
            while s[j] != "#":
                j += 1
            # Extract length
            length = int(s[i:j])
            # Extract the string of that length
            word = s[j+1:j+1+length]
            res.append(word)
            # Move pointer forward
            i = j + 1 + length
        return res
