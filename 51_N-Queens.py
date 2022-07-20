class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        placedCols = []
        res = []
        def place(row: int, vert: int, ldiag: int, rdiag: int) -> None:
            if row == n:
                board = []
                for col in placedCols:
                    board.append('.'*(col) + 'Q' + '.'*(n-col-1))
                res.append(board)
                return
            
            for col in range(n):
                vertMask = 1 << col
                ldiagMask = 1 << (row + col)
                rdiagMask = 1 << (col - row + n-1)
                if vert & vertMask or ldiag & ldiagMask or rdiag & rdiagMask: continue
                placedCols.append(col)
                place(row + 1, vert | vertMask, ldiag | ldiagMask, rdiag | rdiagMask)
                placedCols.pop()
        
        place(0,0,0,0)
        return res