class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        list_length = len(matrix)
        kth_smallest = []

        for index in range(list_length):
            heappush(kth_smallest, (matrix[index][0], index, 0))

        numbers_checked, smallest_number = 0, 0
        while kth_smallest:  
            smallest_number, list_index, num_index = heappop(kth_smallest)
            numbers_checked += 1

            if numbers_checked == k:
                break

            if num_index + 1 < len(matrix[list_index]):
                heappush(kth_smallest, (matrix[list_index][num_index + 1], list_index, num_index + 1))

        return smallest_number


        