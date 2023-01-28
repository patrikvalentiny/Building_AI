import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading

    # Please write your code inside this function

    # read in the training data and separate it to x_train and y_train
    x_train = np.genfromtxt(StringIO(train_string))[:, 0:5]
    y_train = np.genfromtxt(StringIO(train_string))[:, -1]
    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train)[0]

    # read in the test data and separate x_test from it
    x_test = np.genfromtxt(StringIO(test_string))[:, 0:5]

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
