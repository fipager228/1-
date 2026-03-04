import numpy as np
print(np.__version__)

arr1 = np.random.randint(0, 5, size=(3,3))
print(arr1)

print(sum(np.diagonal(np.fliplr(arr1))))

    # np.fliplr - отзеркаливает arr1
    # np.diag и np.diagonal - отовляет диагональ
    # sum - сумирует