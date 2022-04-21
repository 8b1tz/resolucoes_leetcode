from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        triangle = []
        for column_index in range(numRows):
            i += 1
            row_list = []
            valor = 0
            for row_index in range(i):
                if row_index == 0 or row_index == len(triangle):
                    number = 1
                else:
                    number = (
                        triangle[column_index - 1][valor]
                        + triangle[column_index - 1][valor + 1]
                    )
                    valor += 1
                row_list.append(number)
            triangle.append(row_list)
        return triangle
