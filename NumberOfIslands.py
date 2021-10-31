class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
  
        numberOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

#         def dfs(grid, r, c):
           
#             if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!='1'): return
#             grid[r][c] = '0'
#             dfs(grid, r+1,c)
#             dfs(grid, r-1,c)
#             dfs(grid, r,c+1)
#             dfs(grid, r,c-1)

        def bfs(grid, r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                # row, col = q.popleft() #bfs
                row, col = q.pop() #dfs
                dirs = [[1,0],[-1,0],[0,-1],[0,1]]
                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc
                    if(r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visited): 
                        q.append((r,c))
                        visited.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    # dfs(grid, r, c)
                    bfs(grid, r, c)
                    numberOfIslands += 1
       
        
        return numberOfIslands
        
    
        