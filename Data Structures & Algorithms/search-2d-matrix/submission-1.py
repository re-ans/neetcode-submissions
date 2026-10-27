class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            # check the endpoints first
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                l = 0
                r = len(matrix[0]) - 1

                while l <= r:
                    mid_col = l + ((r - l) // 2)
                    if target < matrix[mid][mid_col]:
                        r = mid_col - 1
                    elif target > matrix[mid][mid_col]:
                        l = mid_col + 1
                    else:
                        return True
                return False
        
        return False