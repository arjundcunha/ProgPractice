def getperi(grid, x,y, le,br):
    total = 4
    if x-1>=0:
        if grid[x-1][y] == 1:
            total -= 1
    if x!= le-1:
        if grid[x+1][y] == 1:
            total -= 1
    if y-1>=0:
        if grid[x][y-1] == 1:
            total -= 1
    if y!= br-1:
        if grid[x][y+1] == 1:
            total -= 1
    return total
            
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        leng = len(grid)
        breat = len(grid[0])
        ans = 0
        for x in range(leng):
            for y in range(breat):
                if grid[x][y] == 1:
                    ans += getperi(grid, x,y, leng, breat)
        return ans
        