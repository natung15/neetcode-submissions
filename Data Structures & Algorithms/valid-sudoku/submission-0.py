class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for x in range(0,9)]
        column = [[] for x in range(0,9)]
        grid = [[] for x in range(0,9)]
        
        for i,x in enumerate(board):#iterate through rows - i is the increment / row #
            for j, y in enumerate(x):#iterate through columns in the row - j is the increment / column #
                if y == '.':
                    continue
                box = (i // 3) * 3 + j // 3
                if y in row[i] or y in column[j] or y in grid[box]:
                    return False
                row[i].append(y)
                column[j].append(y)
                grid[box].append(y)
        return True
                