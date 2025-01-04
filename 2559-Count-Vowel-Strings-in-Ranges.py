from itertools import accumulate 

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v=[0]*len(words)
        for i,word in enumerate(words):
            start=word[0]
            end=word[-1]
            vowel_set = {'a','e','i','o','u'}
            if start in vowel_set and end in vowel_set:
                v[i]=1
        prefix_sum= list(accumulate(v))
        print(prefix_sum)
        out =[0]*len(queries)
        for i,qr in enumerate(queries):
            l=qr[0]
            r=qr[1]

            if l == r:
                out[i]=v[l]
            else:
                out[i] =  prefix_sum[r]- (0 if l-1 < 0 else prefix_sum[l-1])
        return out



        