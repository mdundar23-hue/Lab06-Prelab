def list_rotate(list1: list, k: int) -> list:
    """
    Rotate the list cyclically to the right if k is positive, and to the left if k is negative.

    Parameters:
        list1 (list): The list to rotate.
        k (int): The number of positions to rotate the list.

    Returns:
        list: The rotated list.
    """

    if not list1 or len(list1) <=1:
        return list1
    n= len(list1)
    k= k%n 
    if k == 0 :
        return list1
    return list1[-k:] + list1[:-k]
    