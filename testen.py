import Board
import Disk
import copy
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

assert not Board.is_to_explode(test_board_6, (2, 2))
assert not Board.is_to_explode(test_board_6, (5, 1))









