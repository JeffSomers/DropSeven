# Positions identify individual cells on game boards.

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
    pass


def is_overflow_position(dimension,position):
    """
        Check whether the given position is an overflow position for any board
        with the given dimension.
        - True if and only if the position is in the overflow row of the given board.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


def get_all_adjacent_positions(dimension, positions):
    """
        Return a mutable set of all positions adjacent to at least one of the positions
        in the given collection of positions and within the boundaries of any board
        with the given dimension.
        ASSUMPTIONS
        - Each position in the given collection of positions is a proper position
          for any board with the given dimension.
    """
    pass