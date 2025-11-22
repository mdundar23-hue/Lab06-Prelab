def element_frequency(list1: list) -> list:
    """
    Compresses a list by replacing consecutive repeated elements with tuples of the elements and its count.

    Parameters:
        list1 (list): The list of integers.

    Returns:
        list: The compressed list.
    """

    if not list1:
        return []

    compressed_list = []
    current_count = 1

    for i in range(1, len(list1)):
        if list1[i] == list1[i - 1]:
            current_count += 1
        else:
            compressed_list.append((list1[i - 1], current_count))
            current_count = 1

    compressed_list.append((list1[-1], current_count))

    return compressed_list

