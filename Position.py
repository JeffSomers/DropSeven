# Positions identify individual cells on game boards.
def column(position):
    """
    :param position:
    :return: gives back the the column of the position (in this case by returning the
    first element).
    """
    return position[0]

def row (position):
    """
    :param position:
    :return: gives back the the row of the position (in this case by returning the
    second element).
    """
    return position[1]



def is_proper_position(dimension, position):
    """
        Check whether the given position is a proper position for any board
        with the given dimension.
        - The given position must be a tuple of length 2 whose elements are both
          natural numbers.
        - The first element identifies the column. It may not exceed the given
          dimension.
        - The second element identifies the row. It may not exceed the given
          dimension incremented with 1 (taking into account the overflow position)
        ASSUMPTIONS
        - None
    """
    Max_Row= dimension + 1
    Max_Column= dimension
    if len(position) != 2:
        return False
    elif column(position) > Max_Column or row(position) > Max_Row:
        return False
    elif column(position) <=0 or row(position) <= 0:
        return False
    elif isinstance(position, tuple) is False:
        return False
    return True


def is_overflow_position(dimension,position):
    """
        Check whether the given position is an overflow position for any board
        with the given dimension.
        - True if and only if the position is in the overflow row of the given board.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """
    Overflow_row = dimension + 1
    if row(position) == Overflow_row:
        return True
    return False



def left(dimension, position):
    """
        Return the position on any board with the given dimension immediately to
        the left of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """
    copy_list_position = list(position)
    if column(copy_list_position) == 1:
        return None
    else:
        copy_list_position[0] -= 1
        changed_position = tuple(copy_list_position)
        return changed_position




def right(dimension, position):
    """
       Return the position on any board with the given dimension immediately to
       the right of the given position.
       - None is returned if the generated position is outside the boundaries of
         a board with the given dimension.
       ASSUMPTIONS
       - The given position is a proper position for any board with the
         given dimension.
     """
    copy_list_position = list(position)
    if column(copy_list_position) == dimension:
        return None
    else:
        copy_list_position[0] += 1
        changed_position = tuple(copy_list_position)
        return changed_position


def up(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        above the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """
    copy_list_position = list(position)
    max_row = dimension + 1
    if row(copy_list_position) == max_row:
        return None
    else:
        copy_list_position[1] += 1
        changed_position = tuple(copy_list_position)
        return changed_position


def down(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        below the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """
    copy_list_position = list(position)
    if row(copy_list_position) == 1:
        return None
    else:
        copy_list_position[1] -= 1
        changed_position = tuple(copy_list_position)
        return changed_position


def next(dimension, position):
    """
        Return the position on any board with the given dimension next to the
        given position.
        - If the given position is not at the end of a row, the resulting position
          is immediately to the right of the given position.
        - If the given position is at the end of a row, the resulting position is
          the leftmost position of the row above. If that next row does not exist,
          None is returned.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """
    Max_Row = dimension + 1
    Max_Column = dimension
    if row(position) == Max_Row and column(position) == Max_Column:
        return None
    elif column(position) == dimension:
        up_position = up(dimension, position)
        copy_list_up_position = list(up_position)
        copy_list_up_position[0] = 1                         ### kan ik hier niet de kolom van nemen?????
        mostleft_up_position = tuple(copy_list_up_position)
        return mostleft_up_position
    else:
        return right(dimension, position)


def get_all_adjacent_positions(dimension, positions):
    """
        Return a mutable set of all positions adjacent to at least one of the positions
        in the given collection of positions and within the boundaries of any board
        with the given dimension.
        ASSUMPTIONS
        - Each position in the given collection of positions is a proper position
          for any board with the given dimension.
    """
    adjacent_positions = set()

    for one_position in positions:
        possible_Left_positions = left(dimension,one_position)
        if possible_Left_positions is not None:
            adjacent_positions.add(possible_Left_positions)

        possible_Right_positions = right(dimension, one_position)
        if possible_Right_positions is not None:
            adjacent_positions.add(possible_Right_positions)

        possible_Up_positions = up(dimension, one_position)
        if possible_Up_positions is not None:
            adjacent_positions.add(possible_Up_positions)

        possible_Down_positions = down(dimension, one_position)
        if possible_Down_positions is not None:
            adjacent_positions.add(possible_Down_positions)

    return adjacent_positions


