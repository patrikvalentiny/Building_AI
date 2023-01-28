import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100],
              [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for i, coeff in enumerate(c):
        # edit here: calculate the sum of squared error with coefficient set coeff and
        # keep track of the one yielding the smallest squared error
        sse = squared_error(X, y, coeff)
        if sse < smallest_error:
            smallest_error = sse
            best_index = i

    print("the best set is set %d" % best_index)


def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        # add your code here: calculate the predicted price,
        diff = np.dot(xi, c)
        # subtract it from the actual price yi,
        diff = yi - diff
        # square the difference using (yi - prediction)**2,
        diff = diff ** 2
        # and add up all the differences in variable sse
        sse += diff

    return sse


find_best(X, y, c)
