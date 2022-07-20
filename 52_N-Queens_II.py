class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        
        def place(row: int, ldiag: int, rdiag: int, vert: int):
            # placed all queens
            if row == n:
                self.res += 1
                return
            
            for col in range(n):
                ldiagMask, rdiagMask, vertMask = 1 << (row+col), 1 << (col-row+n-1), 1 << col
                if ldiag & ldiagMask or rdiag & rdiagMask or vert & vertMask: continue
                place(row + 1, ldiag | ldiagMask, rdiag | rdiagMask, vert | vertMask)
                
        place(0,0,0,0)
        return self.res