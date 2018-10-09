###############################################################################
# STUDENTS:  IGNORE THIS MODULE (file).
# We use it in our testing code to make error messages appear in color.
###############################################################################

###############################################################################
# The code in this module is a simplified version of code written by:
#     dablak  (https://stackoverflow.com/users/1329248/dablak)
# That code appears at:
#    http://xsnippet.org/359377/
# and is referenced in dablak's question at:
#  https://stackoverflow.com/questions/20333674/pycharm-logging-output-colours.

# As with all user content to StackOverflow, it is licensed (by dablak) under:
#     CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
# a Creative Commons Attribution Share Alike license, as is this code.
###############################################################################

import sys
import time

# Set  USE_COLORING  to False to use the "old" way of printing:
USE_COLORING = True

COLOR_CODES = {'black': 20,
               'red': 31,
               'green': 32,
               'yellow': 33,
               'blue': 34,
               'magenta': 35,
               'cyan': 36,
               'white': 37
               }


def print_result_of_test(expected, actual):
    if USE_COLORING:
        print_it = print_colored
    else:
        print_it = print_uncolored
    try:
        if expected == actual:
            print_it("  PASSED the above test -- good!", color='blue')
        else:
            print_it("  *** FAILED the above test. ***", color='red')
    except Exception:
        print_it("_it  *** FAILED the above test. ***", color='red')


# noinspection PyUnusedLocal
def print_colored(*args, color='black', flush=True):
    text = ""
    for arg in args:
        text = text + " " + str(arg)
    text = text.replace(" ", "", 1) + "\n"
    sys.stdout.write('\033[%sm%s\033[0m' % (COLOR_CODES[color], text))


def print_uncolored(*args, color=None, flush=True):
    if color == 'red':
        print(end='', flush=flush)
        time.sleep(1)
        print(*args, file=sys.stderr, flush=flush)  # Stderr MIGHT be red
    else:
        print(*args, flush=flush)
