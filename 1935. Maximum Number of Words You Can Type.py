class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        h = { ch for ch in brokenLetters }
        wc =0 
        arr = text.split(' ')
        for word in arr:
            for ch in word:
                if ch in h:
                    wc+=1
                    break
        return len(arr) -wc

        