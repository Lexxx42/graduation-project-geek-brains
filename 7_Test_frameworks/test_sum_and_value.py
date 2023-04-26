"""Making first test scripts."""


class TestWithPytest:
    """This class provides data for tests."""
    big_number: int = -191
    numbers: list[int] = [1, 2, 3, 4, 5]

    def test_sum_of_list_elements_equals_fifteen(self) -> None:
        """Test that sum of list elements is equal to 15."""
        input_list = self.numbers
        total = sum(input_list)
        assert total == 15, \
            f"The sum of the list {input_list} is incorrect. " \
            f"Expected: 15. Got: {total}."

    def test_number_is_greater_than_five(self) -> None:
        """Test that the number is greater than 5."""
        number = self.big_number
        assert number > 5, \
            f"Number {number} is not greater than 5."
