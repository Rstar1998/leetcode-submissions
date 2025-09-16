class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) > len(b):
            b= "0"* (len(a)-len(b)) + b
        elif len(b) > len(a):
            a= "0"* (len(b)-len(a)) + a
        else:
            pass

        x = len(a)-1
       
        cr =0
        out =""
        while x >=0:
            if cr == 0:
                if a[x] == '1' and b[x] == '1':
                    out = "0"+out
                    cr =1
                elif a[x] == '0' and b[x] == '0':
                    out = "0"+out
                else:
                    out = "1"+out
            else:
                if a[x] == '1' and b[x] == '1':
                    out = "1"+out
                    cr =1
                elif a[x] == '0' and b[x] == '0':
                    out = "1"+out
                    cr=0
                else:
                    out = "0"+out
                    cr=1
            x-=1
        
        if cr == 1:
            return "1"+out
        else:
            return out



        