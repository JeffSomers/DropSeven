
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