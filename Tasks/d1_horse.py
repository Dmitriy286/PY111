from functools import lru_cache

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    @lru_cache
    def get_steps(i, j):
        row = shape[0]
        col = shape[1]

        if i == 0 and j == 0:
            return 1

        if not 0 <= i < row:
            return 0

        if not 0 <= j < col:
            return 0

        return sum([get_steps(i - 2, j + 1), get_steps(i - 2, j - 1), get_steps(i - 1, j - 2), get_steps(i + 1, j - 2)])
    return get_steps(point[0], point[1])


if __name__ == '__main__':
    assert 13309 == calculate_paths((7, 15), (6, 14))
    assert 2 == calculate_paths((4, 4), (3, 3))

    #     row = shape[0]
    #     col = shape[1]
    #
    #     if i == 0 and j == 0:
    #         return 1
    #
    #     if not 0 <= i < row:
    #         return 0
    #
    #     if not 0 <= j < col:
    #         return 0
    #
    #     return sum([get_steps(i - 2, j + 1),
    #                 get_steps(i - 2, j - 1),
    #                 get_steps(i - 1, j - 2),
    #                 get_steps(i + 1, j - 2)
    #                 ])
    #
    # return get_steps(point[0], point[1])

#
# if __name__ == '__main__':
#     assert 13309 == calculate_paths((7, 15), (6, 14))
#     assert 2 == calculate_paths((4, 4), (3, 3))




