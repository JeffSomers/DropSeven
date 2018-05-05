import Disk
import Board
import Position
import copy
def drop_disk_at(board, disk=None, column=None, Times_exploded=1):
    """
        Drop the given disk on top of the given column in the given board.
        - All disks on the given board that are to explode after having
          dropped the given disk explode effectively, and all non-visible
          disks adjacent to the exploding disks are cracked.
        - Subsequently, disks that are to explode in the new state of the
          board explode effectively, with all non-visible disks
          adjacent to the exploding disks being cracked. This process
          continues until the given board is stable again, i.e. until
          the given board has no more disks to explode.
        - The function returns the total score resulting from the given
          step. That score is calculated as the sum of the product of
          the number of exploding disks in each explosion step with the score
          for a single exploding disk in the given step.
        - If the given disk and/or the given column is None, no disk is
          dropped on the given board. However, disks on the given board
          explode and crack as described above.
        ASSUMPTIONS
        - The given board is a playable board
        - The given column is either None or it is a proper column for
          the given board.
        - The given disk is either None or it is a proper disk for the given
          board and it is not cracked.
        - The given column is not completely filled with disks.
    """
    #1. First place the disk on the given column if disk or column is not None
    if disk is not None or column is not None:
        Board.add_disk_on_column(board,disk,column)
    #2. Make a set of all disks that ar able to explode
    Disks_position_to_explode = Board.get_all_positions_to_explode(board)
    #3. Make a list of all disks that can explode together(all adjacets)
    Disks_position_near_explosion = \
        set(Position.get_all_adjacent_positions(Board.dimension(board), Disks_position_to_explode))
    #4. Crack all posible disk near by an explosion
    Board.crack_disks_at(board,Disks_position_near_explosion)
    #5. Remove the disks that exploded
    Board.remove_all_disks_at(board, Disks_position_to_explode)
    #6. Do it again if still set need to explode
    New_Disks_position_to_explode = Board.get_all_positions_to_explode(board)
    if len(New_Disks_position_to_explode) == 0:
        return Times_exploded*2*len(Disks_position_to_explode)
    else:
        return Times_exploded*2*len(Disks_position_to_explode)+drop_disk_at(board, None, None, Times_exploded*2)





def best_drop_for_disk(board,disk):
    """
       Drop the given disk on the given board in the best possible column.
       - Dropping the disk in any other column of the given board yields a score
         that is not above the score obtained from dropping the given disk in
         the selected column.
       - The function returns a tuple consisting of the column in which the
         given disk has been dropped followed by the actual score obtained
         from that drop.
       - If the same highest score can be obtained from several columns, the
         function drops the disk in the rightmost of these columns.
        ASSUMPTIONS
        - The given board is a playable board that can accept a disk, and the
          given disk is not cracked and it is a proper disk for the given board.
    """
    #1. Get a list of all the columns with there score's by using a copy board
    score_of_columns = []
    for column in range(1,Board.dimension(board)+1):
        copy_board = Board.get_board_copy(board)
        copy_disk = copy.deepcopy(disk)
        if Board.is_full_column(board, column) is False:
            score_of_columns.append((drop_disk_at(copy_board,copy_disk,column),column))
    #2. Sort the list from low to high
    Low_to_High_score = sorted(score_of_columns)
    #3. Chose the last element of the list
    Column_highest_score=Low_to_High_score[-1][1]
    return (Column_highest_score,drop_disk_at(board,disk,Column_highest_score))


def highest_greedy_score(board,disks, First_Time = True, score=None,columns=None):
    """
       Compute the highest possible score that can be obtained by dropping each
       of the given disks on the given board in a greedy way.
       - The disks must be dropped in the order in which they appear in the
         given list of disks. Each disk is dropped in the best column as
         computed by the function best_drop_for_disk.
       - Upon exit from the function, the board reflects the state obtained from
         dropping the disks. If not all the given disks can be dropped because
         the board gets completely filled, the function only drops the disks it can
         drop.
       - The function returns a tuple of (1) the highest score followed by (2) a tuple
         of columns in which the successive disks have been dropped.
       - Upon return, the given list of disks only stores disks that have not been
         dropped on the board.
       - The function will not take into account possible raises of level while
         dropping disks, i.e. the resulting score only reflects scores obtained
         from dropping disks as computed by the function drop_disk_at.
       - This function must be implemented in a RECURSIVE way.
        ASSUMPTIONS
        - The given board is a playable board, and each of the given disks is a
          proper disk for the given board.
        - None of the given disks is cracked.
    """
    if First_Time == True:
        score = 0
        columns = ()
        return highest_greedy_score(board, disks, False, score, columns)

    elif (len(disks) == 0 or Board.can_accept_disk(board) is False) and First_Time == False:
        return (score, columns)
    else:
        disk_to_place = disks[0]
        best_score_column = best_drop_for_disk(board,disk_to_place)
        score_best_disk = best_score_column[1]
        column_best_disk = best_score_column[0]
        score += score_best_disk
        columns += (column_best_disk,)
        del disks[0]
        return highest_greedy_score(board, disks, False, score, columns)



def highest_score(board, disks, First_Time= True, column = None):
    """
       Compute the highest possible score that can be obtained by dropping each
       of the given disks on the given board.
       - The disks must be dropped in the order in which they appear in the
         given sequence of disks.
       - Upon exit from the function, the given board must be in the same state
         as the state it was in upon entry to the function.
       - The function returns a tuple of (1) the highest score followed by (2) a list
         of columns in which the successive disks must be dropped. If not all the
         given disks kan be dropped on the given board, the function returns the tuple
         (None,None).
       - If the same highest score is obtained by dropping some disk in columns
         C1, C2, ..., Ck, the leftmost of these columns is used.
       - Upon return, the given sequence of disks will still store the same disks
         in the same order, and none of these disks has changed its state.
       - The function will not take into account possible raises of level while
         dropping disks, i.e. the resulting score only reflects scores obtained
         from dropping disks as computed by the function drop_disk_at.
        ASSUMPTIONS
        - The given board is a playable board, and each of the given disks is a
          proper disk for the given board.
        - None of the given disks is cracked.
    """
    if First_Time is True and len(disks)==0:
        return (0,())
    ###er van uit gaan dat ze allemaal gaan
    if len(disks) == 0 and First_Time is False:
        return 0
    else:
        highest_score_so_far = 0
        best_columns_so_far = [Board.dimension(board)]
            for position in range(1,Board.dimension(board)+1):
                column =  [position]
                copy_board = Board.get_board_copy(board)
                score_disk = drop_disk_at(copy_board, disks[0], position)+highest_score(copy_board,disks[1:], False, column)
                if (score_disk > highest_score_so_far) or (score_disk == highest_score_so_far and column < best_columns_so_far):
                    highest_score_so_far = score_disk
                    best_columns_so_far = column
            return (highest_score_so_far,best_columns_so_far)






def play(board,disks_to_drop=[],columns=[],wrapped_disks_to_insert=()):
    """
    Play the game on the given board using the disks to drop, the wrapped
    disks to insert and the columns to drop the disks on.
    - As soon as the sequence of columns is exhausted, the function prompts
      the user to enter the column of his/her choice.
    - The function returns the total score obtained from dropping all the given
      disks. If all disks cannot be dropped, the function returns None.
    ASSUMPTIONS
    - The given board is a playable board that can accept a new disk.
    - Each disk in the sequence of disks to drop is a proper disk for any board
      with the same dimension as the given board, and whose state is either VISIBLE
      or WRAPPED.
    - Each disk in the sequence of wrapped disks to insert is a proper disk for any board
      with the same dimension as the given board. The state of each disk is WRAPPED.
      The number of disks in the sequence is a multiple of the dimension of the
      given board.
    - Each of the given columns is a proper column for the given board.
    """
    assert Board.is_proper_board(board) and Board.can_accept_disk(board)
    assert all(map(lambda disk:
        Disk.is_proper_disk(Board.dimension(board),disk),disks_to_drop))
    assert all(map(lambda disk:
        Disk.get_state(disk) in {Disk.VISIBLE,Disk.WRAPPED},disks_to_drop))
    assert all(map(lambda disk:
        Disk.is_proper_disk(Board.dimension(board),disk),wrapped_disks_to_insert))
    assert all(map(lambda disk:
        Disk.get_state(disk) == Disk.WRAPPED,wrapped_disks_to_insert))
    assert len(wrapped_disks_to_insert) % Board.dimension(board) == 0
    assert all(map(lambda col: 1<= col <= Board.dimension(board),columns))
    turns_per_level = 20
    total_score = 0
    current_nb_turns = 0
    columns_to_use = list(columns)
    while (len(disks_to_drop) > 0) and Board.can_accept_disk(board):
        if len(columns_to_use) == 0:
            selected_column = int(input("Identify column to drop disk: "))
        else:
            selected_column = list.pop(columns_to_use,0)
        if Board.is_full_column(board,selected_column):
            return None
        disk_to_drop = list.pop(disks_to_drop,0)
        total_score += drop_disk_at(board,disk_to_drop,selected_column)
        current_nb_turns += 1
        if current_nb_turns == turns_per_level and Board.can_accept_disk(board):
            total_score += 1000 // turns_per_level
            Board.inject_bottom_row_wrapped_disks(board)
            current_nb_turns = 0
            turns_per_level = max(turns_per_level-1,10)
    return total_score
