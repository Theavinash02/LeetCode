class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[-1])
        total =m*n

        results = [n*[0] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old_id = i*n+ j  # covert 2d to 1d

                new_id = (old_id+k)%total

                new_row= new_id//n
                new_col = new_id%n

                results[new_row][new_col] = grid[i][j]

        return results