# approach 1 brute force

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output_list=[]
        i=0
        while i <= len(searchWord)-1:
            temp_word = searchWord[0:i+1]
            temp_list=[]
            for stri in products:
                if stri.startswith(temp_word):
                    temp_list.append(stri)
            temp_list.sort()
            output_list.append(temp_list[:3])
            i+=1
        return output_list
        
# approach 2

