import Board
import Disk
import copy
import Position
import Drop7
import Drop7_Test
wrapped_disk_value_1 = None
wrapped_disk_value_1_B = None
wrapped_disk_value_1_C = None
wrapped_disk_value_1_D = None
wrapped_disk_value_2 = None
wrapped_disk_value_2_B = None
wrapped_disk_value_2_C = None
wrapped_disk_value_2_D = None
wrapped_disk_value_2_E = None
wrapped_disk_value_3 = None
wrapped_disk_value_3_B = None
wrapped_disk_value_3_C = None
wrapped_disk_value_3_D = None
wrapped_disk_value_3_E = None
wrapped_disk_value_4 = None
wrapped_disk_value_4_B = None
wrapped_disk_value_5 = None
visible_disk_value_1 = None
visible_disk_value_1_B = None
visible_disk_value_2 = None
visible_disk_value_2_B = None
visible_disk_value_3 = None
visible_disk_value_3_B = None
visible_disk_value_3_C = None
visible_disk_value_3_D = None
visible_disk_value_4 = None
visible_disk_value_4_B = None
visible_disk_value_4_C = None
visible_disk_value_5 = None
visible_disk_value_5_B = None
visible_disk_value_5_C = None
visible_disk_value_5_D = None
visible_disk_value_5_E = None
visible_disk_value_5_F = None
visible_disk_value_5_G = None
visible_disk_value_6 = None
visible_disk_value_6_B = None
cracked_disk_value_1 = None
cracked_disk_value_1_B = None
cracked_disk_value_2 = None
cracked_disk_value_2_B = None
cracked_disk_value_3 = None
cracked_disk_value_3_B = None
cracked_disk_value_4 = None
cracked_disk_value_4_B = None
cracked_disk_value_4_C = None
cracked_disk_value_5 = None
test_board_4 = None
test_board_4_alias = None
test_board_6 = None
test_board_6_alias = None


def set_up():
    global \
        wrapped_disk_value_1, wrapped_disk_value_1_B, wrapped_disk_value_1_C, \
        wrapped_disk_value_1_D, wrapped_disk_value_2, wrapped_disk_value_2_B, \
        wrapped_disk_value_2_C, wrapped_disk_value_2_D, wrapped_disk_value_2_E, \
        wrapped_disk_value_3, wrapped_disk_value_3_C, wrapped_disk_value_3_D, \
        wrapped_disk_value_3_B, wrapped_disk_value_3_E, wrapped_disk_value_4, \
        wrapped_disk_value_4_B, wrapped_disk_value_5, \
        visible_disk_value_1, visible_disk_value_1_B, visible_disk_value_2, \
        visible_disk_value_2_B, visible_disk_value_3, visible_disk_value_3_B, \
        visible_disk_value_3_C, visible_disk_value_3_D, visible_disk_value_4, \
        visible_disk_value_4_B, visible_disk_value_4_C, visible_disk_value_5, \
        visible_disk_value_5_B, visible_disk_value_5_C, visible_disk_value_5_D, \
        visible_disk_value_5_E, visible_disk_value_5_F, visible_disk_value_5_G, \
        visible_disk_value_6, visible_disk_value_6_B, \
        cracked_disk_value_1, cracked_disk_value_1_B, cracked_disk_value_2, \
        cracked_disk_value_2_B, cracked_disk_value_3, cracked_disk_value_3_B, \
        cracked_disk_value_4, cracked_disk_value_4_B, cracked_disk_value_4_C, \
        cracked_disk_value_5, \
        test_board_4, test_board_4_alias, test_board_6, test_board_6_alias

    wrapped_disk_value_1 = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_1_B = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_1_C = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_1_D = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_2 = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_B = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_C = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_D = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_2_E = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_3 = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_B = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_C = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_D = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_E = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_4 = Disk.init_disk(Disk.WRAPPED, 4)
    wrapped_disk_value_4_B = Disk.init_disk(Disk.WRAPPED, 4)
    wrapped_disk_value_5 = Disk.init_disk(Disk.WRAPPED, 5)

    visible_disk_value_1 = Disk.init_disk(Disk.VISIBLE, 1)
    visible_disk_value_1_B = Disk.init_disk(Disk.VISIBLE, 1)
    visible_disk_value_2 = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_2_B = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_3 = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_B = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_C = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_D = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_4 = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_4_B = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_4_C = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_5 = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_B = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_C = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_D = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_E = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_F = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_5_G = Disk.init_disk(Disk.VISIBLE, 5)
    visible_disk_value_6 = Disk.init_disk(Disk.VISIBLE, 6)
    visible_disk_value_6_B = Disk.init_disk(Disk.VISIBLE, 6)

    cracked_disk_value_1 = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_1_B = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_2 = Disk.init_disk(Disk.CRACKED, 2)
    cracked_disk_value_2_B = Disk.init_disk(Disk.CRACKED, 2)
    cracked_disk_value_3 = Disk.init_disk(Disk.CRACKED, 3)
    cracked_disk_value_3_B = Disk.init_disk(Disk.CRACKED, 3)
    cracked_disk_value_4 = Disk.init_disk(Disk.CRACKED, 4)
    cracked_disk_value_4_B = Disk.init_disk(Disk.CRACKED, 4)
    cracked_disk_value_4_C = Disk.init_disk(Disk.CRACKED, 4)
    cracked_disk_value_5 = Disk.init_disk(Disk.CRACKED, 5)

    test_board_4 = Board.init_board \
        (dimension=4, given_disks= \
            ((wrapped_disk_value_3,),
             [],
             (cracked_disk_value_2, cracked_disk_value_1, wrapped_disk_value_2, visible_disk_value_3)))

    test_board_4_alias = Board.init_board \
        (dimension=4, given_disks= \
            ((wrapped_disk_value_3,),
             [],
             (cracked_disk_value_2, cracked_disk_value_1, wrapped_disk_value_2, visible_disk_value_3)))

    test_board_6 = Board.init_board \
        (dimension=6, given_disks= \
            ((wrapped_disk_value_3,),
             (wrapped_disk_value_3_B, visible_disk_value_4),
             (visible_disk_value_5, visible_disk_value_4_B, visible_disk_value_1),
             (visible_disk_value_1_B, cracked_disk_value_1, visible_disk_value_6,
              wrapped_disk_value_3_C, cracked_disk_value_1_B),
             (),
             (wrapped_disk_value_3_D, visible_disk_value_3)))

    test_board_6_alias = Board.init_board \
        (dimension=6, given_disks= \
            ((wrapped_disk_value_3,),
             (wrapped_disk_value_3_B, visible_disk_value_4),
             (visible_disk_value_5, visible_disk_value_4_B, visible_disk_value_1),
             (visible_disk_value_1_B, cracked_disk_value_1, visible_disk_value_6,
              wrapped_disk_value_3_C, cracked_disk_value_1_B),
             (),
             (wrapped_disk_value_3_D, visible_disk_value_3)))



set_up()
test_board = Board.init_board \
    (dimension=2, given_disks= \
        ([cracked_disk_value_1, ],
         [cracked_disk_value_1_B, ]))
test_board_alias = Board.init_board \
    (dimension=2, given_disks= \
        ([cracked_disk_value_1, ],
         [cracked_disk_value_1_B, ]))
test_board_copy = Board.get_board_copy(test_board)
highest_score, columns = \
    Drop7.highest_score(test_board, [wrapped_disk_value_1, wrapped_disk_value_2, visible_disk_value_1])
assert highest_score is None
assert columns is None
assert Drop7_Test.are_identical_boards(test_board, test_board_alias)
assert Drop7_Test.are_equal_boards(test_board, test_board_copy)












