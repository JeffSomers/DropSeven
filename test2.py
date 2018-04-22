import Board
import Disk
import copy
import Position
wrapped_disk_value_1 = None
wrapped_disk_value_2 = None
wrapped_disk_value_3 = None
wrapped_disk_value_3_B = None
wrapped_disk_value_3_C = None
wrapped_disk_value_5 = None
visible_disk_value_1 = None
visible_disk_value_2 = None
visible_disk_value_2_B = None
visible_disk_value_3 = None
visible_disk_value_3_B = None
visible_disk_value_4 = None
visible_disk_value_6 = None
cracked_disk_value_1 = None
cracked_disk_value_1_B = None
cracked_disk_value_3 = None
cracked_disk_value_4 = None
test_board_4 = None
test_board_6 = None

def set_up():
    """
       This function initializes a large number of disks and two boards
       that can be used in tests. Such a test will then start with an
       invocation of this function
    """
    global\
        wrapped_disk_value_1, wrapped_disk_value_2, wrapped_disk_value_3, \
                wrapped_disk_value_3_C, wrapped_disk_value_3_B, wrapped_disk_value_5, \
        visible_disk_value_1, visible_disk_value_2, visible_disk_value_2_B, \
                visible_disk_value_3, visible_disk_value_3_B, visible_disk_value_4, \
                visible_disk_value_6, \
        cracked_disk_value_1, cracked_disk_value_1_B, cracked_disk_value_3, \
                cracked_disk_value_4, \
        test_board_4, test_board_6

    wrapped_disk_value_1 = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_2 = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_3 = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_B = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_C = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_5 = Disk.init_disk(Disk.WRAPPED, 5)

    visible_disk_value_1 = Disk.init_disk(Disk.VISIBLE, 1)
    visible_disk_value_2 = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_2_B = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_3 = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_B = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_4 = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_6 = Disk.init_disk(Disk.VISIBLE, 6)

    cracked_disk_value_1 = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_1_B = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_3 = Disk.init_disk(Disk.CRACKED, 3)
    cracked_disk_value_4 = Disk.init_disk(Disk.CRACKED, 4)
    test_board_4 = Board.init_board \
        (dimension=4, given_disks= \
            ((wrapped_disk_value_3,),
             [],
             (visible_disk_value_1, cracked_disk_value_1, wrapped_disk_value_2, visible_disk_value_3)))

    test_board_6 = Board.init_board \
        (dimension=6, given_disks= \
            ((wrapped_disk_value_3,),
             [wrapped_disk_value_3_B, wrapped_disk_value_5],
             (visible_disk_value_6, visible_disk_value_3_B, wrapped_disk_value_1),
             (visible_disk_value_1, cracked_disk_value_1,
                    visible_disk_value_4, visible_disk_value_3),
             (cracked_disk_value_1_B,),
             [wrapped_disk_value_3_C, visible_disk_value_2_B]))


set_up()

print(set_disk_at(test_board_4, (1,2),wrapped_disk_value_1 ))
print(test_board_4)



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
    ## Check if it is None to be safe
    if disk == None:
        disk_to_change = Board.get_disk_at(board,position)
        print(disk_to_change)
        if Disk.is_proper_disk(Board.dimension(board), disk_to_change) is True:
            ###check if if rows in the same columns above have a disk
            for row_pos in range(position[0]+1,Board.dimension(board)+1):
                if Board.get_disk_at(board,(position[0],row_pos)) is None:
                    return False
    # 1) change the position in the coordinates in the matrix
    column = position[0] - 1
    print(column)
    row = Board.dimension(board) - (position[1] - 1)
    return (board[row][column])
