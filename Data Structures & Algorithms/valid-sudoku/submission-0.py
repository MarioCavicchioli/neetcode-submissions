class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):     
            appeared = set()     
            for j in range(9):      
                cell = board[i][j]

                if cell == ".": continue
                
                if cell in appeared:
                    return False

                appeared.add(cell)

        for m in range(9):     
            appeared2 = set()     
            for n in range(9):      
                cell2 = board[n][m]

                if cell2 == ".": continue
                
                if cell2 in appeared2:
                    return False      

                appeared2.add(cell2)    

        for r in range(3):              # box row: 0, 1, 2
            for c in range(3):          # box column: 0, 1, 2
                appeared = set()        # fresh set for each box
                for di in range(3):     # row inside the box
                    for dj in range(3): # column inside the box
                        cell = board[3*r + di][3*c + dj]
                        if cell == ".": continue
                
                        if cell in appeared:
                            return False  

                        appeared.add(cell)  

        return True 