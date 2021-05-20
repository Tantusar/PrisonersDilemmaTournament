# CATCHUP by Tantusar
#
# Attempt to keep the average of my moves
# and my opponent's moves as close as possible.

def strategy(history, memory):

    choice = 0

    if history.shape[1] == 0 or history[1].sum() >= history[0].sum():
        choice = 1

    return choice, None
