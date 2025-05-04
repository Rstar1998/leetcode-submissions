class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            
            if carry == 0:
                break
            temp=digits[i]+carry
            
            digits[i]=temp%10
            carry=temp//10
        
        if carry == 1:
            return [1]+digits
        else:
            return digits

        