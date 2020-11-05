class Solution:
    def findNeighbors(self, coordinates, grid):
        '''Function to fetch the immediate neighbors of a point in the grid'''
        neighbors = []
        m = len(grid)
        n = len(grid[0])
        i = coordinates[0]
        j = coordinates[1]

        # Check upward
        if i!=0 and grid[i-1][j]=="1":
            neighbors.append((i-1, j))
        # Check downward
        if i<m and grid[i+1][j]=="1":
            neighbors.append((i+1, j))
        # Check right
        if j<m and grid[i][j+1]=="1":
            neighbors.append((i, j+1))
        # Check left
        if j!=0 and grid[i][j-1]=="1":
            neighbors.append((i, j-1))

        return neighbors
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.findNeighbors((0,0), grid)
        