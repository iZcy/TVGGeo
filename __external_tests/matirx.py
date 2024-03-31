import numpy as np

matrixObj = np.array([[-1, 1, 0], [-1, 1, 0], [-1, -1, 0], [1, 1, 0]])
matrixTrans = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

matrixRes = np.dot(matrixObj, matrixTrans)
print(matrixRes)