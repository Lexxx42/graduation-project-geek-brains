"""Making first test scripts."""
import unittest


class TestWithUnittest(unittest.TestCase):
    """Test class must be inherited from TestCase."""
    big_number = -191
    numbers = [1, 2, 3, 4, 5]

    def test_sum_of_list_elements_equals_fifteen(self) -> None:
        """Test that sum of list elements is equal to 15."""
        input_list = self.numbers
        total = sum(input_list)
        self.assertEqual(total, 15, \
                         f"The sum of the list {input_list} is incorrect. " \
                         f"Expected: 15. Got: {total}.")

    def test_number_is_greater_than_five(self) -> None:
        """Test that the number is greater than 5."""
        number = self.big_number
        self.assertTrue(number > 5, \
                        f"Number {number} is not greater than 5.")


if __name__ == "__main__":
    """This method works if started from that module."""
    unittest.main()
    print("All tests passed!")
