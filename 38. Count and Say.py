class Solution:
    def countAndSay(self, n: int) -> str:

        def count_rle(s):
            rle=""
            curr_char=s[0]
            count=1
            if len(s) == 1:
                return str(count)+curr_char

            for i in range(1,len(s)):
                if s[i] == curr_char:
                    count+=1
                else:
                    rle+=str(count)+curr_char
                    curr_char = s[i]
                    count=1

                if i == len(s)-1:
                        rle+=str(count)+curr_char
            return rle

              
        cur_rle ="1"
        if n > 1:
            i = 1
            while i <= n-1:
                cur_rle=count_rle(cur_rle)
                
                i+=1
       
        return cur_rle
        