class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.strip("/").split("/")
    

        st=[]

        for i in path_arr:
            
            if i == '' or i == '.':
                continue 

            if i == "..":
                if len(st)>0:
                    st.pop()
                continue
            st.append(i)
        print(st)
        return  '/' + '/'.join(st)
        