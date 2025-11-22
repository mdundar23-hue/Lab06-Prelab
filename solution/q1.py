def is_sublist(list1: list, list2: list) -> bool:
    """
    Check if list2 is a sublist of list1.

    Parameters:
        list1 (list): The list to check if list2 is a sublist of.
        list2 (list): The list to check if it is a sublist of list1.

    Returns:
        bool: True if list2 is a sublist of list1, False otherwise.
    """

    if not list2:
        return True
    if len(list2) > len(list1):
        return False

    for i in range(len(list1) - len(list2) + 1):
        match = True
        for j in range(len(list2)):
            if list1[i + j] != list2[j]:
                match = False
                break
        if match:
            return True

    return False
