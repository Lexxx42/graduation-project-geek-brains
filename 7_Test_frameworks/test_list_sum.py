"""Making first test scripts."""


def test_sum_of_list_elements_equals_fifteen(input_list: list[int]) -> None:
    """Test that sum of list elements is equal to 15."""
    total = sum(input_list)
    assert total == 15, \
        f"The sum of the list {input_list} is incorrect. " \
        f"Expected: 15. Got: {total}."


def test_number_is_greater_than_five(number: int) -> None:
    """Test that the number is greater than 5."""
    assert number > 5, \
        f"Number {number} is not greater than 5."


if __name__ == "__main__":
    """This method works if started from that module."""
    big_number = -191
    test_number_is_greater_than_five(big_number)
    numbers = [1, 2, 3, 4, 5]
    test_sum_of_list_elements_equals_fifteen(numbers)
    print("All tests passed!")
