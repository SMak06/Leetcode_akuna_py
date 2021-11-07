class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose and then reverse
        
#         self.transpose(matrix)
#         self.reverse(matrix)
        
#     def transpose(self, matrix):
#         for i in range(len(matrix)):
#             for j in range(i, len(matrix)):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
#     def reverse(self, matrix):
#         for i in range(len(matrix)):
#             for j in range(len(matrix) // 2):
#                 matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        matrix[:] = map(list, zip(*matrix[::-1]))