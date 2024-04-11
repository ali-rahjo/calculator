import unittest
from typing import NoReturn

from src.calculator import Calculator
from src.custom_ex import IncorrectInputError, DivideNotCorrect

import operator

class CalculatorAddTestCase(unittest.TestCase):  # Test Case

    def test_add_3_corrrect_input(self) -> None | NoReturn:  # Unit
        # Arrange
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 8

        # Act
        result = calculator.add(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_no_args(self) -> None | NoReturn:
        # Arrange
        calculator = Calculator()
        expected_result = 0

        # Act
        result = calculator.add()

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_incorrect_input(self) -> NoReturn:
        # Arrange
        calculator = Calculator()
    def setUp(self):
        self.calculator = Calculator()
    def test_div_with_correct_input(self):
         calculator = Calculator()
        #Arrange
        x = 4
        y = 2
        expected_result = 2

        #Act
        result = self.calculator.division(x, y)

        # Assert 
        self.assertEqual(result, expected_result)

    def tearDown(self):
            pass
        x = "6"
        y = [4, 5]

        # Act/Assert
        with self.assertRaises(TypeError):
            calculator.add(x, y)


class CalculatorMultTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_mult_with_correct_input(self):
        # Arrange
        x = 1
        y = 2
        z = 3
        expected_result = 6

        # Act
        result = self.calculator.multiply(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_mult_with_incorrect_input(self):
        # Arrange
        x = []
        y = (1, 2)
        z = "4"

        # Act/Assert
        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x, y, z)

    def tearDown(self):
        pass

class CalculatorDivisionTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_divi_with_correct_input(self):
        calculator = Calculator()
        #Arrange
        x = 4
        y = 2
        expected_result = 2

        #Act
        result = self.calculator.division(x, y)

        # Assert 
        self.assertEqual(result, expected_result)

    def test_divide_by_zero(self):

        self.calculator = Calculator()
    def test_divi_with_correct_input(self):
         calculator = Calculator()
        #Arrange
        x = 4
        y = 2
        expected_result = 2

        #Act
        result = self.calculator.division(x, y)

        # Assert 
        self.assertEqual(result, expected_result)

    def tearDown(self):
            pass
        #Arrange 
        x = 4
        y = 0
    
        #act/assert
        with self.assertRaises(DivideNotCorrect):
            self.calculator.division(x, y)


    def tearDown(self):
        pass


class CalculatorSubsTestCase(unittest.TestCase):  # Test Case

    def test_subs_3_corrrect_input(self) -> None | NoReturn:  # Unit
        # Arrange
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 0

        # Act
        result = operator.sub()

        # Assert
        self.assertEqual(result, expected_result)
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 0

def test_sub_with_no_args(self) -> None | NoReturn:
        # Arrange
        calculator = Calculator()
        expected_result = 0

        # Act  def test_div_with_correct_input(self):
        calculator = Calculator()
        #Arrange
        x = 4
        y = 2
        expected_result = 2

        #Act
        result = self.calculator.division(x, y)

        # Assert 
        self.assertEqual(result, expected_result)
