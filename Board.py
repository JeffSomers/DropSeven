# Boards are square areas of N rows and N columns.
#     - Rows and columns in boards are numbered starting from 1.
import Disk
import Position
import copy
import random
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
#    if isinstance(board,list) is False:           ###is deze voorwaarde nodig
#        return False
    if board == None:
        return False
    elif dimension(board) <= 0:
        return False

    for row in board:
        for cell in row:
            if cell is not None and Disk.is_proper_disk(dimension(board),cell) is False:
                return False
    return True




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
    #The given board is a proper board.
    if is_proper_board(board) is False:
        return False
    #If a cell stores a disk, all cells below also store a disk.
    nb_of_rows = len(board)
    for row_position in range(nb_of_rows -1):
        row = board[row_position]                                     ###Last row doesn't need to be checked!
        for disk_position in range(len(row)):
            disk = board[row_position][disk_position]
            if Disk.is_proper_disk(dimension(board), disk) is True:
                row_underneath = row_position+1
                investigated_disk= board[row_underneath][disk_position]   ###checking if the disk underneath is not None
                if Disk.is_proper_disk(dimension(board), investigated_disk) is False:
                    return False
    #The same disk is not stored at several positions on the given board.
    #1) first store every not-none disk in a list
    all_disks_without_none= []
    for row in board:
        for disk in row:
            if disk != None:
                all_disks_without_none.append(disk)

    for pos_disk1 in range(len(all_disks_without_none)):
        for pos_disk2 in range(len(all_disks_without_none)):
            if pos_disk1 != pos_disk2 and all_disks_without_none[pos_disk1] is all_disks_without_none[pos_disk2]:
                return False
    return True







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
    ###1) Make a board with the asked dimension all filled with None
    number_of_rows = dimension + 1
    number_of_columns = dimension
    # determine the length of the matrix
    Matrix = [0] * number_of_rows
    # All columns are None
    for i in range(number_of_rows):
        Matrix[i] = [None] * number_of_columns
    ###2) fill the sequences in the board
    sequence_position = 0
    while sequence_position < len(given_disks):
        disk_position = 0
        sequence = given_disks[sequence_position]
        while disk_position < len(sequence):
            Matrix[dimension - disk_position][sequence_position] = given_disks[sequence_position][disk_position]
            disk_position += 1
        sequence_position += 1
    return Matrix


def get_board_copy(board):
    """
      Return a full copy of the given board.
      - The resulting copy contains copies of the disks stored
         on the original board.
      ASSUMPTIONS
      - The given board is a proper board.
    """
    copy_board = copy.deepcopy(board)
    return copy_board


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
    #check for a board
    if not isinstance(board, (list,tuple)):
        return None
    if len(board)==0:
        return None
    nb_rows = len(board)
    nb_columns = None

    for row in range(0,nb_rows):

        if not isinstance(board[row],
                          (list,tuple,str,range)):
            return None
        if (nb_columns == None):
            nb_columns = len(board[row])
        elif (len(board[row]) != nb_columns):
            return None
    else:
        return nb_columns



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
    if isinstance(board,list) is False:
        return None
    if isinstance(position, tuple) is False:
        return None
    if Position.is_proper_position(dimension(board), position) is False:
        return None
    #1) change the position in the coordinates in the matrix
    column_board_position = position[0]-1
    row_board_position = dimension(board)-(position[1]-1)
    ###None is returned if there is no disk at the given position.
    disk = board[row_board_position][column_board_position]
    if disk == None:
        return None
    ###None is returned if position out of boundries or proper position
    if Position.is_proper_position(dimension(board), position) is False:
        return None
    ###None if board is not proper

    return board[row_board_position][column_board_position]


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
    ### Check if it is None to be safe
    # if disk == None and Position.is_overflow_position(dimension(board),position) is False:
    #     disk_to_change = get_disk_at(board,position)
    #     if Disk.is_proper_disk(dimension(board), disk_to_change) is True:
    #         ###check if if rows in the same columns above have a disk
    #         for row_pos in range(position[1]+1,dimension(board)+2):  ###from row pos to end including overflow
    #             if get_disk_at(board,(position[0],row_pos)) != None:
    #                 return False

    # 1) change the position in the coordinates in the matrix
    column_board_position = position[0] - 1
    row_board_position = dimension(board) - (position[1] - 1)
    board[row_board_position][column_board_position] = disk



def has_disk_at(board, position):
    """
        Check whether a disk is stored at the given position on the given board.
        - The function returns false if no disk can be obtained from the given
          board at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for that board.
    """
    disk = get_disk_at(board,position)
    if Disk.is_proper_disk(dimension(board),disk) is False:
        return False
    return True


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
    row_under_overflow = dimension(board)
    for row in range(1,row_under_overflow+1):
        if get_disk_at(board,(column,row)) == None:
            return False
    return True


def is_full_column_with_overflow(board, column):    ###TODO: andere beschrijving geven
    """
       Check whether the non-overflow part of the given column on the given board
       is completely filled with disks.
       - The overflow cell of a full column may also contain a disk, but it may
         also be empty.
        ASSUMPTIONS
        - The given board is a proper board, and the given column is a proper column
          for that board.
    """
    row_overflow = dimension(board) +1
    for row in range(1,row_overflow+1):
        if get_disk_at(board,(column,row)) == None:
            return False
    return True

def is_disk_in_overflow(board, column):     ###TODO de beschrijving veranderen
    """
       Check whether the non-overflow part of the given column on the given board
       is completely filled with disks.
       - The overflow cell of a full column may also contain a disk, but it may
         also be empty.
        ASSUMPTIONS
        - The given board is a proper board, and the given column is a proper column
          for that board.
    """
    overflow_row = dimension(board) + 1 ###overflow_row from board
    if get_disk_at(board,(column,overflow_row)) == None:
            return False
    return True

def is_full_with_one_overflow(board):     ####TODO de beschrijving veranderen
    """
       Check whether the non-overflow part of the  given board is completely
       filled with disks.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for column in range(1,dimension(board)+1):
        if is_disk_in_overflow(board,column):
            return True
    return False


def is_full(board):
    """
       Check whether the non-overflow part of the  given board is completely
       filled with disks.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for column in range(1,dimension(board)+1):
        if is_full_column(board,column) is False:
            return False
    return True




def can_accept_disk(board):
    """
        Check whether the given board can accept an additional disk.
        - True if and only if (1) all overflow cells of the given board are free,
          and (2) at least one of the cells in the non-overflow portion of the
          given board is free.
        ASSUMPTIONS
        - The given board is a proper board.

    """
    if is_full_with_one_overflow(board) is False and is_full(board) is False:
        return True
    return False


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
    if is_full_column_with_overflow(board,column):
        return board
    else:
        for row in range(1, dimension(board)+2):
            if get_disk_at(board,(column,row)) == None:
                set_disk_at(board,(column,row),disk)
                return board

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

    ###change all disks in column one position above
    for row in range(dimension(board)+1,1,-1):
        position_to_change= (column,row)
        set_disk_at(board,position_to_change,get_disk_at(board,(Position.down(dimension(board),position_to_change))))
    ### Change the in first row
    set_disk_at(board,(column,1),disk)


def inject_bottom_row_wrapped_disks(board):
    """
        Insert a bottom row of wrapped disks in the given board.
        - All disks already in the board are shifted up one position.
        - No disk on the given board will explode yet, even if the conditions
          for having an explosion are satisfied.
        ASSUMPTIONS
        - The given board is a playable board that can accept a disk.
    """
    for column in range(1,dimension(board)+1):
        inject_disk_in_column(board,Disk.init_disk(Disk.WRAPPED,random.randint(0,dimension(board))), column)


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

    if Position.is_overflow_position(dimension(board), position):
        set_disk_at(board,position,None)
    elif get_disk_at(board,position) == None:
        return
    elif Position.row(position) == dimension(board):
        set_disk_at(board,position, get_disk_at(board,Position.up(dimension(board), position)))
        set_disk_at(board,Position.up(dimension(board), position),None)
        return
    else:
        set_disk_at(board, position, get_disk_at(board, Position.up(dimension(board), position)))
        remove_disk_at(board,(Position.column(position),Position.row(position)+1))




def get_length_vertical_chain(board, position, row_down=0):
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
    column = position[0]
    column_board_position = column - 1
    row_down += 1
    row_Down_board_position = dimension(board) - (row_down - 1)
    if get_disk_at(board, position)  == None:
        return 0
    if board[row_Down_board_position][column_board_position] == None:    ###TODO: verander dit ook in een get disk weet niet hoe
        return 0
    if row_down == len(board)+1:
        if get_disk_at(board,(column,row_down)) == None:
            return 0
        else:
            return 1
    else:
        return 1 + get_length_vertical_chain(board, position, row_down)


def get_length_horizontal_chain(board, position, State_count = None):
    """
        Return the length of the horizontal chain of disks involving the given
        position. Zero is returned if no disk is stored at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for the given board.
    """
    disk_column_position = Position.column(position)
    row = position[1]
    row_board_position = dimension(board) - (row - 1)
    disks = []
    if get_disk_at(board,position) == None:
        return 0
    row_in_board = board[row_board_position]
    Dict_disk = {}
    for disk_position in range(len(row_in_board)):
        disk = row_in_board[disk_position]
        if Disk.is_proper_disk(dimension(board), disk):
            disks.append(disk)
            Dict_disk.update({disk_position+1:disk})
            State_count = True
        if disk == None and State_count == True:
            if disk_column_position in Dict_disk.keys():
                return len(disks)
            else:
                State_count = None
                disks = []

    return len(disks)

###TODO: nog zien dat je de vorige def kunt gebruiken


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
    disk_to_check = get_disk_at(board,position)
    if disk_to_check == None:
        return False
    Disk_value =  Disk.get_value(disk_to_check)
    Disk_state = Disk.get_state(disk_to_check)
    if (Disk_value == get_length_vertical_chain(board, position) or Disk_value ==
        get_length_horizontal_chain(board, position)) and Disk_state == Disk.VISIBLE:
        return True
    return False


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
    if start_pos == (dimension(board),dimension(board)+1):
        if is_to_explode(board,start_pos):
            return frozenset({start_pos})
        else:
            return frozenset({})
    elif is_to_explode(board,start_pos):
        return frozenset({start_pos}).union(get_all_positions_to_explode(board, Position.next(dimension(board), start_pos)))
    else:
        return frozenset({}).union(get_all_positions_to_explode(board,Position.next(dimension(board), start_pos)))



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
    for position in positions:
        if Disk.is_proper_disk(dimension(board),get_disk_at(board,position)):
            disk = get_disk_at(board,position)
            if Disk.get_state(disk) == Disk.WRAPPED:
                Disk.set_state(disk,Disk.CRACKED)
            elif Disk.get_state(disk) == Disk.CRACKED:
                Disk.set_state(disk,Disk.VISIBLE)





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
    list_positions=list(positions)
    ###ordering the list from highest row to lowest row
    sorted_positions = sorted(list_positions)
    sorted_positions =sorted_positions[::-1]
    for position in sorted_positions:
        remove_disk_at(board,position)



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
