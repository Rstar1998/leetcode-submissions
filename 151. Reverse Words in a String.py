class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        arr=s.split(" ")

        while "" in arr:
            arr.remove("")
            
        print(arr)
        low=0
        high=len(arr)-1

        while low <= high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp 
            low+=1
            high-=1
        
        return " ".join(arr)

        