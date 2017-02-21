"""
Calculator.py provides functionality of a calculator as different functions. The main class
Calculator encapsulates all the functionality as different functions
"""


class Calculator(object):
    """
    Calculator class
    """

    def add(self, num1, num2):
        """
        Returns addition of num1 and num2 if num1 and num2 are integers,floats,long,double
        :param num1: first parameter
        :param num2: second parameter
        :return: num1+num2
        """
        if isinstance(num1, str) or isinstance(num2, str):
            raise TypeError("Invalid Type: {} and {}".format(type(num1), type(num2)))
        else:
            return num1 + num2


if __name__ == '__main__':  #pragma: no cover
    calc = Calculator()
    print("10 + 20 = {} ".format(calc.add(10, 20)))
