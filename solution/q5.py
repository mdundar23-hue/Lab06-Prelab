def hidden_sequence_len(list1: list) -> int:
    """
    Finds the length of the longest subsequence of consecutive numbers.

    Parameters:
        list1 (list): The list of integers.

    Returns:
        int: The length of the longest subsequence of consecutive numbers.
    """

    if not list1:
        return 0

    max_length = 1

    for num in list1:
        current_length = 1
        current_num = num

        while True:
            next_num = current_num + 1
            if next_num not in list1:
                break
            current_length += 1
            current_num = next_num

        max_length = max(max_length, current_length)

    return max_length
