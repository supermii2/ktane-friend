MODULE_NAME = "maze"
CLASS_NAME = "ModuleMaze"

class ModuleMaze():
    SIZE = 6

    MAZES = [

    ]


    def __init__(self, device):
        self.device = device
        self.memory = []
        self.visited = [[0 for x in range(ModuleMaze.SIZE)] for y in range(ModuleMaze.SIZE)] 

    def hasUpWall(self, grid, x, y):
        return grid[x][y] % 2 == 1
    
    def hasLeftWall(self, grid, x, y):
        return grid[x][y] // 2 % 2 == 1
    
    def hasRightWall(self, grid, x, y):
        return grid[x][y] // 4 % 2 == 1
    
    def hasDownWall(self, grid, x, y):
        return grid[x][y] // 8 % 2 == 1

    def solveMaze(self, grid, xOrig, yOrig, xTarget, yTarget):
        grid[xOrig][yOrig] = 1
        if xOrig == xTarget and yOrig == yTarget:
            return True
        
        if not self.hasUpWall(grid, xOrig, yOrig) and not self.visited[xOrig - 1][yOrig]:
            return True if self.solveMaze(grid, xOrig - 1, yOrig, xTarget, yTarget) else False
        
        if not self.hasLeftWall(grid, xOrig, yOrig) and not self.visited[xOrig][yOrig - 1]:
            return True if self.solveMaze(grid, xOrig, yOrig - 1, xTarget, yTarget) else False    
        
        if not self.hasUpWall(grid, xOrig, yOrig) and not self.visited[xOrig + 1][yOrig]:
            return True if self.solveMaze(grid, xOrig + 1, yOrig, xTarget, yTarget) else False  
                  
        if not self.hasRightWall(grid, xOrig, yOrig) and not self.visited[xOrig][yOrig + 1]:
            return True if self.solveMaze(grid, xOrig, yOrig + 1, xTarget, yTarget) else False   

        return False
    
    def handle(self, word):
        #TODO: Add check
        self.memory.append(int(word))
        
