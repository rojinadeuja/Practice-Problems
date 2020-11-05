import queue

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
        if i<m-1 and grid[i+1][j]=="1":
            neighbors.append((i+1, j))
        # Check right
        if j<n-1 and grid[i][j+1]=="1":
            neighbors.append((i, j+1))
        # Check left
        if j!=0 and grid[i][j-1]=="1":
            neighbors.append((i, j-1))

        return neighbors
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        que = queue.Queue()
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0" :
                    que.put((i,j))
                    while not que.empty():
                        coord = que.get()
                        children = self.findNeighbors(coord, grid)
                        for child in children:
                            que.put(child)
                            grid[child[0]][child[1]] = "0"
                        grid[coord[0]][coord[1]] = "0"
                    islands+=1
                    print("Found Island")
            
        return islands

 # Time complexity is O(i*j) where i = number of rows and j = number of columns
 # Space complexity is O(i*j)       