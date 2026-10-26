class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # n = len(board)
        seen_rows = [set() for _ in range(9)]
        seen_cols = [set() for _ in range(9)]
        seen_squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                square = (r // 3) * 3 + (c // 3)
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen_rows[r] or board[r][c] in seen_cols[c] or board[r][c] in seen_squares[square]:
                    return False
                seen_rows[r].add(board[r][c])
                seen_cols[c].add(board[r][c])
                seen_squares[square].add(board[r][c])

        return True
