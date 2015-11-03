__author__ = 'sb5518'

"""This class corresponds to question 1. It prints 5 arrays,
the first one is the generic version and the rest are answers to questions a), b), c) and d) in that order """

import numpy as np


class question_1:
    @staticmethod
    def question1():  #This function prints the answer to question 1 when called

        try:
            array1 = (np.arange(15)+1).reshape(3, 5).transpose()

            array2 = array1[[1, 3]]

            array3 = array1[:, 1]

            array4 = array1[1:4, 0:3]

            array5 = np.array(filter(lambda x: 2<x and x<12, array1.T.reshape(1, 15)[0]))


            print array1
            print array2
            print array3
            print array4
            print array5

        except ArithmeticError as e:
            print "Arithmetic Error: ", e
        except LookupError as e:
            print "Lookup error: ", e