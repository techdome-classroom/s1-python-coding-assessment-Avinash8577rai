class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid),len(grid[0])
        
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        
        #Helper function

        def DFS(r,c):
            #Base case
            if r<0 or c<0 or r>=rows or c>= cols:
                return
            if grid[r][c]=='W' or visited[r][c]:
                return
            
            visited[r][c]=True
            
            #Checking all four direction
            
            DFS(r+1,c)
            DFS(r-1,c)
            DFS(r,c+1)
            DFS(r,c-1)
        
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] =='L' and not visited[i][j]:
                    DFS(i,j)
                    count+=1             
        return count