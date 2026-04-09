def transpose_tuples(matrix: list[tuple]) -> list[tuple]:
    """
    Manipulates a matrix by transposing it.

    Parameters:
        matrix (list[tuple]): The matrix to manipulate.

    Returns:
        list[tuple]: The transposed matrix.
    """

    # TODO: Implement the function
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    result = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            element = matrix[row][col]
            new_row.append(element)
        result.append(tuple(new_row))
    return result
    