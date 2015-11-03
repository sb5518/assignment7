__author__ = 'sb5518'
import numpy as np

"""This class corresponds to question 3. It prints 1 array that answers the question. """

class question_3:
    @staticmethod
    def question3(): #This function prints the answer to question 3 when called

        try:
            ran = np.random.uniform(low=0, high=1, size=(30,))
            mask_array = np.random.uniform(low=0, high=1, size=(30,))
            array1 = ran.reshape(10, 3)
            mask_array = mask_array.reshape(10, 3)
            array2 = array1.copy()
            print array2

            for i in range(0, len(array1)):
                array1[i] = array1[i] - [0.5, 0.5, 0.5]

            array1 = np.absolute(array1)

            distance_array = np.argsort(array1)

            distance_array = distance_array[:, 0]

            for i in range(0, len(array2)):
                x = distance_array[i]
                mask_array[i, x] = 1

            mask_array = (mask_array == 1)

            final_array = array2[mask_array].copy()

            print final_array

        except ArithmeticError as e:
            print "Arithmetic Error: ", e
        except LookupError as e:
            print "Lookup error: ", e