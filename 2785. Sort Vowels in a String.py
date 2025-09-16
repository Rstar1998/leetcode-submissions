from collections import deque
class Solution:
    def sortVowels(self, s: str) -> str:
        st=[]
        st_arr = list(s)  

        for i in range(len(st_arr)):
            if st_arr[i] in ('a','e','i','o','u','A','E','I','O','U'):
                st.append(st_arr[i])
                st_arr[i]="*"
        
        st.sort()

        dq = deque(st)

        for i in range(len(st_arr)):
            if st_arr[i] == "*":
                st_arr[i] = dq.popleft()

        return ''.join(st_arr)

       
        