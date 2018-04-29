# Disks can be stored on the game board. They have a state
# and a number.
#  - Disks are mutable things. More in particular, it must be
#    possible to change the state of a disk.

# Enumeration of the possible states of a disk.
VISIBLE = 10
CRACKED = 20
WRAPPED = 30
import random

def is_proper_disk(dimension, disk):
    """
       Check whether the given disk is a proper disk for any board with
       the given dimension.
       - The state of the given disk must be one of the values VISIBLE,
         WRAPPED, CRACKED or some additional self-defined state.
       - The value of the given disk must be a positive integer number
         that does not exceed the dimension of the given board.
       ASSUMPTIONS
       - None
    """
    if disk ==  None:
        return False
    value = disk[1]
    state = disk[0]

    if value < 0 or value > dimension:
        return False
    elif isinstance(value , int) is False:
        return False
    elif state not in [VISIBLE, WRAPPED, CRACKED]:
        return False

    return True



def init_disk(state, value):
    """
       Return a new disk with given state and given value.
       ASSUMPTIONS
       - None
    """
    return [state,value]


def get_random_disk(dimension,possible_states):
    """
       Return a random disk for a board with the given dimension with
       a state that belongs to the collection of possible states.
       ASSUMPTIONS
       - The given dimension is positive.
       - The given collection of possible states is not empty and contains
         only elements VISIBLE, WRAPPED and/or CRACKED
    """
    value= random.randint(1,dimension)
    state= random.choice(list(possible_states))
    return [state, value]



def set_state(disk, state):
    """
        Set the state of the given disk to the given state.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    disk[0] = state


def get_state(disk):
    """
        Return the state of the given disk.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    return disk[0]


def set_value(disk, value):
    """
        Set the value of the given disk to the given value.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """

    disk[1] = value

def get_value(disk):
    """
        Return the value of the given disk.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    return disk[1]


def get_disk_copy(disk):
    """
        Return a new disk whose state and value are identical to the
        state and value of the given disk.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """
    return list(disk)