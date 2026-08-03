class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenSquares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in seenRow[row] or board[row][col] in seenCol[col] or board[row][col] in seenSquares[(row//3,col//3)]):
                    return False
                seenRow[row].add(board[row][col])
                seenCol[col].add(board[row][col])
                seenSquares[(row//3,col//3)].add(board[row][col])
        return True