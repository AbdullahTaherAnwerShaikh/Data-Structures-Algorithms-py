class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for entry in range(9):
                if board[row][entry] == ".":
                    continue
                elif board[row][entry] in seen:
                    return False
                else:
                    seen.add(board[row][entry])
        for col in range(9):
            seen = set()
            for entry in range(9):
                if board[entry][col] == ".":
                    continue
                elif board[entry][col] in seen:
                    return False
                else:
                    seen.add(board[entry][col])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True