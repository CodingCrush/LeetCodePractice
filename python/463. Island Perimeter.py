class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def cal_element_perimeter(row, column):
            element_perimeter = 0
            limited_rows = list(range(len(grid)))
            limited_columns = list(range(len(grid[0])))
            for n_row, n_column in (
                    (row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
                if n_row not in limited_rows or n_column not in limited_columns:
                    element_perimeter += 1
                else:
                    if grid[n_row][n_column] == 0:
                        element_perimeter += 1
            return element_perimeter

        perimeter = 0
        for row, row_group in enumerate(grid):
            for column, element in enumerate(row_group):
                if element:
                    perimeter += cal_element_perimeter(row, column)
        return perimeter
