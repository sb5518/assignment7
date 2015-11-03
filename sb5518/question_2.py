__author__ = 'sb5518'
import numpy as np

"""This class corresponds to question 1. It prints 1 array that answers the question """

np.seterr(divide = "raise") #This is used to raise exception when dividing by 0. We will catch that exception later.

class question_2:
    @staticmethod
    def question2(): #This function prints the answer to question 2 when called

        try:
            array1 = np.ones((5, 5))
            array2 = np.array([1., 5, 10, 15, 20])
            array3 = np.arange(25).reshape(5, 5)
            for i in range(5):
                array1[:, i]= array3[  :, i]/array2
            print array1
        except ArithmeticError as e:
            print "Arithmetic Error: ", e
        except LookupError as e:
            print "Lookup error: ", e
