# Boards are square areas of N rows and N columns.
#     - Rows and columns in boards are numbered starting from 1.
import Disk

def is_proper_board(board):
    """
        Check whether the given board is a proper board. The function
        returns true iff all the conditions below are satisfied:
        - The given board may not be None, and its dimension
          must be a natural number.
        - Each cell of the given board either stores nothing (None),
          or it stores a proper disk for the given board.
        ASSUMPTIONS
        - None
    """

    if not dimension(board) => 0:
        return False
    elif board == None:
        return False
    for row in board:
        for cell in row:
            if not isinstance(None, cell):
                return False
            elif is_proper_disk(dimension(board), cell)




def is_playable_board(board):
    """
        Check whether the given board is a playable board. The function
        returns true iff all the conditions below are satisfied:
        - The given board is a proper board.
        - If a cell stores a disk, all cells below also store
          a disk (i.e. there are no gaps in columns).
        - The same disk is not stored at several positions on the given board.
        ASSUMPTIONS
        - None
    """
    pass


def init_board(dimension, given_disks=()):
    """
        Return a new board with given dimension and filled with the given disks.

        - The collection of given disks is a sequence. The element at position I
          in that sequence specifies the disks to be loaded on column I+1 of the
          new board.
        - If there is no matching element for a column, no disks are loaded on
          that column.
        ASSUMPTIONS
        - The given dimension is a positive integer number.
        - The number of elements in the sequence of given disks is between 0
          and the given dimension.
        - Each element of the given sequence of disks is a sequence of
          disks for the new board. The length of each sequence of disks
          is less than or equal to the given dimension incremented with 1.
          Each disk must be a proper disk for the given board.
        NOTE
        - Notice that the resulting board will be a proper board, but not
          necessarily a playable board. Notice also that some disks on the board
          might satisfy the conditions to explode.
    """
    board = []
    ###1) Make a board with the asked dimension all filled with None
    for sequence in given_disks:
        if len(sequence)
    for row in range(0, dimension-1):
        for kolom in row[0]:
            return [row[kolom]]

        board.append(disk_sequence)






def get_board_copy(board):
    """
      Return a full copy of the given board.
      - The resulting copy contains copies of the disks stored
         on the original board.
      ASSUMPTIONS
      - The given board is a proper board.
    """
    pass


def dimension(board):
    """
        Return the dimension of the given board.
        - The dimension of a square board is its number of rows or equivalently
          its number of columns.
        - The function returns None if no dimension can be obtained from the given
          board. This is for instance the case if a string, a number, ... is passed
          instead of a board.
        ASSUMPTIONS
        - None (we must be able to use this function at times the thing that
          is given to us is not necessarily a proper board, e.g. in the function
          is_proper_board itself)
    """
    pass


def get_disk_at(board, position):
    """
        Return the disk at the given position on the given board.
        - None is returned if there is no disk at the given position.
        - The function also returns None if no disk can be obtained from the given
          board at the given position. This is for instance the case if a string,
          a number, ... is passed instead of a board or a position, if the given
          position is outside the boundaries of the given board, ...
        ASSUMPTIONS
        - None (same remark as for the function dimension)
     """
    pass


def set_disk_at(board, position, disk):
    """
        Fill the cell at the given position on the given board with the given disk.
        - The disk nor any other disk will yet explode, even if the conditions
          for having an explosion are satisfied.
        - The given disk may be None, in which case the disk, if any, at the given
          position is removed from the given board, WITHOUT disks at higher positions
          in the column dropping down one position.
        ASSUMPTIONS
        - The given board is a proper board, the given position is a proper
          proper position for the given board and the given disk is a proper
          disk for the given board.
    """
    pass


def has_disk_at(board, position):
    """
        Check whether a disk is stored at the given position on the given board.
        - The function returns false if no disk can be obtained from the given
          board at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for that board.
    """
    pass


def is_full_column(board, column):
    """
       Check whether the non-overflow part of the given column on the given board
       is completely filled with disks.
       - The overflow cell of a full column may also contain a disk, but it may
         also be empty.
        ASSUMPTIONS
        - The given board is a proper board, and the given column is a proper column
          for that board.
    """
    pass


def is_full(board):
    """
       Check whether the non-overflow part of the  given board is completely
       filled with disks.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    pass


def can_accept_disk(board):
    """
        Check whether the given board can accept an additional disk.
        - True if and only if (1) all overflow cells of the given board are free,
          and (2) at least one of the cells in the non-overflow portion of the
          given board is free.
        ASSUMPTIONS
        - The given board is a proper board.

    """
    pass


def add_disk_on_column(board, disk, column):
    """
        Add the given disk on top of the given column of the given board.
        - The disk is registered at the lowest free position in the given column.
          Nothing happens if the given column is completely filled, including the
          overflow cell of that column.
        - The disk nor any other disk will yet explode, even if the conditions for
          having an explosion are satisfied.
        ASSUMPTIONS
        - The given board is a proper board, the given column is a proper column
          for the given board, and the given disk is a proper disk for the given board.
    """
    pass


def inject_disk_in_column(board, disk, column):
    """
        Inject the given disk at the bottom of the given column of the given board.
        - The disk is registered in the bottom cell of the given column, i.e., in the
          cell at row 1.
        - All disks already in the given column are shifted up one position.
        ASSUMPTIONS
        - The given board is a proper board, the given column is a proper column
          for that board whose overflow cell is free, and the given disk is a
          proper disk for the given board.
    """
    pass


def inject_bottom_row_wrapped_disks(board):
    """
        Insert a bottom row of wrapped disks in the given board.
        - All disks already in the board are shifted up one position.
        - No disk on the given board will explode yet, even if the conditions
          for having an explosion are satisfied.
        ASSUMPTIONS
        - The given board is a playable board that can accept a disk.
    """
    pass


def remove_disk_at(board, position):
    """
        Remove the disk at the given position from the given board.
        - All disks above the removed disk drop one position down.
        - Nothing happens if no disk is stored at the given position.
        - No disk will explode yet, even if the conditions for having an
          explosion are satisfied.
        ASSUMPTIONS
        - The given board is a proper board, and the given position is
          a proper position for that board.
        NOTE
        - This function must be implemented in a RECURSIVE way.
    """
    pass


def get_length_vertical_chain(board, position):
    """
        Return the length of the vertical chain of disks involving the given
        position. Zero is returned if no disk is stored at the given position.
        ASSUMPTIONS
        - The given board is a playable board and the given position is a
          proper position for the given
          board.
        NOTE
        - This function must be implemented in a RECURSIVE way.
    """
    pass


def get_length_horizontal_chain(board, position):
    """
        Return the length of the horizontal chain of disks involving the given
        position. Zero is returned if no disk is stored at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for the given board.
    """
    pass


def is_to_explode(board, position):
    """
        Return a boolean indicating whether the disk, if any, at the given
        position on the given board satisfies the conditions to explode.
        - True if and only if (1) the disk at the given position is visible, and
          (2) the number of the disk is equal to the length of the horizontal chain
          and/or the vertical chain involving that position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for the given board.
    """
    pass


def get_all_positions_to_explode(board,start_pos=(1,1)):
    """
        Return a frozen set of all positions on the given board that
        have a disk that satisfies the conditions to explode, starting
        from the given position and proceeding to the top of the board
        using the next function.
        - The function returns the empty set if the given start position
          is None.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given start position is either None or it is a proper position
          for the given board.
        NOTE
        - The second parameter should not be included in the code that
          is given to the students. They must learn to extend functions
          with extra parameters with a default value. The documentation
          of the function must be changed in view of that.
    """
    pass


def crack_disks_at(board, positions):
    """
        Crack all disks at the given positions on the given board.
        - Wrapped disks will become cracked, and cracked disks will become
          visible.
        - Some positions may not contain any disk, or may contain non-crackable
          disks.
        ASSUMPTIONS
        - The given board is a proper board, and each of the given positions
          is a proper position for the given board.
    """
    pass


def remove_all_disks_at(board, positions):
    """
        Remove all disks at the given positions on the given board.
        - All disks on top of disks that are removed drop down.
        - Positions in the given collection of positions at which no disk
          is stored, are ignored.
        ASSUMPTIONS
        - The given board is a proper board, and each of the given positions
          is a proper position for the given board.
    """
    pass


### BOARD HELPER FUNCTIONS ###

def print_board(board):
    """
        Print the given board.
        ASSUMPTIONS
        - The given board must be a proper board.
    """
    assert is_proper_board(board)
    # Formatting could be used to improve the layout.
    for row in range(dimension(board)+1, 0, -1):
        print(end="|")
        for col in range(1, dimension(board) + 1):
            disk = get_disk_at(board, (col, row))
            if disk == None:
                print('   ', end=" |", )
            else:
                status, value = disk
                if status == Disk.WRAPPED:
                    print('%2s' % '\u2B24', end=" |")
                elif status == Disk.CRACKED:
                    print('%4s' % '\u20DD', end=" |")
                else:  # numbered disk
                    print('%3s' % value, end=" |", )
        print()
        if row == dimension(board)+1:
            print("|"+"----|"*dimension(board))
    print()
