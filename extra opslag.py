# if len(disks) == 0 and First_Time ==True:
#     return 0
# disk_to_place = disks[0]
# best_score_column = best_drop_for_disk(Board.get_board_copy(board), disk_to_place)[0]
# best_columns += (best_score_column,)
# if First_Time == None:
#     del disks[0]
#     return ((drop_disk_at(board, disk_to_place, best_score_column) + highest_greedy_score(board, disks,best_columns, True)),(best_columns))
# elif Board.can_accept_disk(board) and len(disks) != 0:
#     del disks[0]
#     return drop_disk_at(board,disk_to_place, best_score_column) + highest_greedy_score(board, disks, best_columns, True)
# if count_score is False and column_count is False:
#     if len(disks) == 0 or Board.can_accept_disk(board) is False:
#         return 0,()
#     copy_board = Board.get_board_copy(board)
#     copy_disks = copy.deepcopy(disks)
#     disk_to_place = disks[0]
#     best_score_column = best_drop_for_disk(Board.get_board_copy(board), disk_to_place)[0]
#     del disks[0]
#     return (drop_disk_at(board,disk_to_place, best_score_column) + highest_greedy_score(board, copy_disks[1:], True, False )),\
#        ((best_drop_for_disk(copy_board, disk_to_place)[0],) + (highest_greedy_score(copy_board,disks, False, True)))
# if Board.can_accept_disk(board) and len(disks) != 0:
#     disk_to_place = disks[0]
#     best_score_column = best_drop_for_disk(Board.get_board_copy(board), copy.deepcopy(disk_to_place))[0]
#     if count_score == True:
#         del disks[0]
#         return drop_disk_at(board,disk_to_place, best_score_column) + highest_greedy_score(board,disks, True, False)
#     elif column_count == True:
#         del disks[0]
#         return (best_drop_for_disk(board, disk_to_place)[0],) + highest_greedy_score(board, disks, False, True)
# else:
#     if count_score is True:
#         return 0
#     elif column_count is True:
#         return ()

# if len(disks) == 0 and First_Time == True:
#     return (0,())