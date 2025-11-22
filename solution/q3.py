def list_rotate(list1: list, k: int) -> list:
    """
    Rotate the list cyclically to the right if k is positive, and to the left if k is negative.

    Parameters:
        list1 (list): The list to rotate.
        k (int): The number of positions to rotate the list.

    Returns:
        list: The rotated list.
    """

    if not list1:
        return list1

    n = len(list1)

    direction = 1 if k > 0 else -1
    k = abs(k) % n

    if k == 0:
        return list1

    if direction > 0:
        for _ in range(k):
            last = list1.pop()
            list1.insert(0, last)
    else:  # rotate left
        for _ in range(k):
            first = list1.pop(0)
            list1.append(first)

    return list1