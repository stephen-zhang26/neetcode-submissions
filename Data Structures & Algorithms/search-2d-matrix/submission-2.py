class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        left, right = 0, Rows * Cols - 1
        while left <= right:
            mid = (left + right)//2
            val = matrix[mid // Cols][mid % Cols]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            elif val > target:
                right = mid -1
        return False

                