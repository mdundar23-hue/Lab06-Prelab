def zigzag_merge(list1: list, list2: list) -> list:
    """
    Merges two lists into a single list in a zigzag manner.

    Parameters:
        list1 (list): The first list to merge.
        list2 (list): The second list to merge.

    Returns:
        list: The merged list.
    """

    # TODO: Implement the function
    result = []
    i = 0
    while i< len(list1) and i < len(list2):
        result.append(list1[i])
        result.append(list2[i])
        i += 1

    while i <len(list1):
        result.append(list1[i])
        i += 1

    while i <len(list2):
        result.append(list2[i])
        i += 1
    return result
    

