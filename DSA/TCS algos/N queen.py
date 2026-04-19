def n_queen(n):
    result = []
    queens = [-1] * n
    def is_safe(row, col):
         