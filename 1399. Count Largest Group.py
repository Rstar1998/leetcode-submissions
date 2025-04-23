from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:

        max_cnt = -1

        hash_ = defaultdict(int)

        for i in range(1,n+1):
            sum_dig = 0
            while i > 0:
                sum_dig+=i%10
                i=i//10
            hash_[sum_dig]+=1
            max_cnt=max(max_cnt,hash_[sum_dig])
        cnt=0


        for k,v in hash_.items():
            if v == max_cnt:
                cnt+=1
        return cnt


        