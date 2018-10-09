"""
Exam 2, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and YUCHEN ZHU  October 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


###############################################################################
# For the problems in this module, you should use (that is, CALL)
# the following   is_prime   function as appropriate.
# READ but do NOT modify this   is_prime   function.
###############################################################################
def is_prime(n):
    """
    What comes in:  A nonnegative integer.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.  (Note: We treat 0 and 1 as NOT prime here.)
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
      -- is_prime(1)  returns  False
    Note: The algorithm used here is simple and clear but slow.
    """
    if n < 2:
        return False
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False
    return True


###############################################################################
# The  main  function and the TODOs for you are after this:
###############################################################################
def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    run_test_problem1a()
    run_test_problem1b()
    run_test_problem1c()
    run_test_problem1d()


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print('Test 1:')
    strings = ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'ab']
    expected = [3, 5, 3, 6, 3, 4, 7, 2]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 2:
    print()
    print('Test 2:')
    strings = ['Four', 'This is ABC', 'onetwo', 'X', '']
    expected = [4, 11, 6, 1, 0]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 3:
    print()
    print('Test 3:')
    strings = ['This is AB', 'not this', '', 'yikes!']
    expected = [10, 8, 0, 6]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 4:
    print()
    print('Test 4:')
    strings = ['help']
    expected = [4]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 5:
    print()
    print('Test 5:')
    strings = []
    expected = []
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 6:
    print()
    print('Test 6:')
    strings = ['']
    expected = [0]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 7:
    print()
    print('Test 7:')
    strings = ['12345', '1234', '1234567890', '123', '12', '1']
    expected = [5, 4, 10, 3, 2, 1]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 8:
    print()
    print('Test 8:')
    strings = ['1234', '1234567890', '123', '12', '1', '123', '123']
    expected = [4, 10, 3, 2, 1, 3, 3]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 9:
    print()
    print('Test 9:')
    strings = ['1234', '1234567890', '123', '12', '1']
    expected = [4, 10, 3, 2, 1]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 10:
    print()
    print('Test 10:')
    strings = ['1234', '1234567890', '1234', '123456', '1']
    expected = [4, 10, 4, 6, 1]
    actual = problem1a(strings)
    print('  This test case calls:')
    print('    problem1a(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)


def problem1a(strings):
    """
    What comes in:
      -- a sequence of strings
    What goes out:
      Returns a list of the lengths of the strings in the given sequence,
      in the same order that the strings are in the sequence.
    Side effects: None.
    Examples:

      If the given sequence of strings is:
          ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'ab']
      then this function returns  [3, 5, 3, 6, 3, 4, 7, 2]

      If the given sequence of strings is:
          ['Four', 'This is ABC', 'onetwo', 'X', '']
      then this function returns  [4, 11, 6, 1, 0]

      If the given sequence of strings is:
          ['This is AB', 'not this', '', 'yikes!']
      then this function returns   [10, 8, 0, 6]

     If the given sequence of strings is ['help']
     then this function returns [4]
     
     If the given sequence of strings is [] (i.e, the empty list),
     then this function returns []
     
     If the given sequence of strings is ['']
     then this function returns [0]
 
    Type hints:
      :type strings: list of str
      :rtype: list of int
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    result = []
    for i in range(len(strings)):
        result += [len(strings[i])]
    return result

def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print('Test 1:')
    strings = ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'ab']
    expected = 6
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 2:
    print()
    print('Test 2:')
    strings = ['Four', 'This is ABC', 'onetwo', 'X', '']
    expected = 1
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 3:
    print()
    print('Test 3:')
    strings = ['This is AB', 'not this', '', 'yikes!']
    expected = 0
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 4:
    print()
    print('Test 4:')
    strings = []
    expected = 0
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 5:
    print()
    print('Test 5:')
    strings = ['12345', '1234', '1234567890', '123', '12', '1', '12345678901']
    expected = 4
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 6:
    print()
    print('Test 6:')
    strings = ['12345', '1234', '1234567890', '123', '12', '1', '123', '123']
    expected = 5
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 7:
    print()
    print('Test 7:')
    strings = ['12345', '1234', '1234567890', '123', '12', '1']
    expected = 3
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 8:
    print()
    print('Test 8:')
    strings = ['1234', '1234567890', '123', '12', '1', '123', '123']
    expected = 4
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 9:
    print()
    print('Test 9:')
    strings = ['1234', '1234567890', '123', '12', '1']
    expected = 2
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 10:
    print()
    print('Test 10:')
    strings = ['1234', '1234567890', '1234', '123456', '1']
    expected = 0
    actual = problem1b(strings)
    print('  This test case calls:')
    print('    problem1b(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)


def problem1b(strings):
    """
    What comes in:
      -- a sequence of strings
    What goes out:
      Returns the number of strings whose length is prime.
      Note: For purposes of this problem, 0 and 1 are treated as NOT prime,
            per the   is_prime  function defined above.
    Side effects: None.
    Examples:

      If the given sequence of strings is:
          ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'ab']
      then this function returns  6  since there are 6 strings whose length
      is prime, namely:
         'two'     (length 3)
         'prime'   (length 5)
         'xxx'     (length 3)
         'yyy'     (length 3)
         'abcabcX' (length 7)
         'ab'      (length 2)

      If the given sequence of strings is:
          ['Four', 'This is ABC', 'onetwo', 'X', '']
      then this function returns  1  since only 'This is ABC'
      has a length (11) that is prime.

      If the given sequence of strings is:
          ['This is AB', 'not this', '', 'yikes!']
      then this function returns   0   since the strings have lengths
      10, 8, 0, and 6, respectively, none of which are prime.

     If the given sequence of strings is [] (i.e, the empty list), then this
     function returns 0 (since no strings in the list have prime length).

    Type hints:
      :type strings: list of str
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    list = problem1a(strings)
    count = 0
    for i in range(len(list)):
        if is_prime(list[i]) is True:
            count += 1
    return count

def run_test_problem1c():
    """ Tests the   problem1c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print('Test 1:')
    strings = ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'ab']
    expected = False  # 6 strings are prime, and 6 is NOT prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 2:
    print()
    print('Test 2:')
    strings = \
        ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'abab']
    expected = True  # 5 strings have prime length, and 5 IS prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 3:
    print()
    print('Test 3:')
    strings = ['In', 'a', 'galaxy']
    expected = False  # 1 string has prime length, and 1 is NOT prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 4:
    print()
    print('Test 4:')
    strings = ['four', 'two', 'prime', 'five']
    expected = True  # 2 strings have prime length, and 2 IS prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 5:
    print()
    print('Test 5:')
    strings = ['12345', '1234', '1234567890', '123', '12', '1', '12345678901']
    expected = False  # 4 strings have prime length, and 4 is NOT prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 6:
    print()
    print('Test 6:')
    strings = ['12345', '1234', '1234567890', '123', '12', '1', '123', '123']
    expected = True  # 5 strings have prime length, and 5 IS prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 7:
    print()
    print('Test 7:')
    strings = ['12345', '1234', '1234567890', '123', '12', '1']
    expected = True  # 3 strings have prime length, and 3 IS prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 8:
    print()
    print('Test 8:')
    strings = ['1234', '1234567890', '123', '12', '1', '123', '123']
    expected = False  # 4 strings have prime length, and 4 is NOT prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 9:
    print()
    print('Test 9:')
    strings = ['1234', '1234567890', '123', '12', '1']
    expected = True  # 2 strings have prime length, and 2 IS prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 10:
    print()
    print('Test 10:')
    strings = ['1234', '1234567890', '1234', '123456', '1']
    expected = False  # 0 strings have prime length, and 0 is NOT prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 11:
    print()
    print('Test 11:')
    strings = []
    expected = False  # 0 strings have prime length, and 0 is NOT prime
    actual = problem1c(strings)
    print('  This test case calls:')
    print('    problem1c(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)


# -----------------------------------------------------------------------------
# IMPORTANT: Your solution to the next problem must use the above functions
# (including possibly your own functions) appropriately, else NO credit for it.
# -----------------------------------------------------------------------------
def problem1c(strings):
    """
    What comes in:
      -- a sequence of strings
    What goes out:
      Returns True if the number of strings whose length is prime is itself
      prime.  (Again, treat 0 and 1 as NOT prime.)
    Side effects: None.
    Examples:

      If the given sequence of strings is:
          ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'ab']
      then this function returns
          False
      since there are 6 strings whose length is prime, and 6 is NOT prime.

      If the given sequence of strings is:
         ['two', 'prime', 'xxx', 'abcabc', 'yyy', 'xxxx', 'abcabcX', 'abab]
      then this function returns
         True
      since there are 5 strings (namely: two  prime  xxx  yyy  abcabcX)
      whose length is prime, and 5 is prime.

      If the given sequence of strings is:
          ['In', 'a', 'galaxy']
      this function returns
          False
      since there is 1 string ('In') whose length is prime, and 1 is NOT prime.

      If the given sequence of strings is:
          ['four', 'two', 'prime', 'five']
      then this function returns
          True
      since there are 2 strings (namely:  two  prime)
      whose length is prime, and 2 is prime.

     If the given sequence of strings is [] (i.e, the empty list),
      then this function returns
          False
     since there are 0 strings whose length is prime, and 0 is NOT prime.

    Type hints:
      :type strings: list of str
      :rtype: bool
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    # See  IMPORTANT  note before the DEF line of this function.
    # -------------------------------------------------------------------------
    if is_prime(problem1b(strings)) is True:
        return True
    else:
        return False


def run_test_problem1d():
    """ Tests the   problem1d   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1d   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print('Test 1:')
    strings = ['1234', '1234567890', '123', '12', '1', '123', '123']
    expected = '123'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 2:
    print()
    print('Test 2:')
    strings = \
        ['ab', '1234567890', '123', '12', '1', '123', '123']
    expected = 'ab'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 3:
    print()
    print('Test 3:')
    strings = \
        ['1234', '1234567890', '1234', '12345678', '1', '', '12345678901']
    expected = '12345678901'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 4:
    print()
    print('Test 4:')
    strings = ['1234', '1234567890', '1234', '12345678', '1', '']
    expected = -1
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 5:
    print()
    print('Test 5:')
    strings = []
    expected = -1
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 6:
    print()
    print('Test 6:')
    strings = ['', '1234', '1234567890', '1234567', '12', '1', '123', '123']
    expected = '1234567'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 7:
    print()
    print('Test 7:')
    strings = ['', '1', '1234567890', '12', '1', '123', '123']
    expected = '12'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 8:
    print()
    print('Test 8:')
    strings = ['12345', '1234567', '123', '12345678901']
    expected = '12345'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 9:
    print()
    print('Test 9:')
    strings = ['1234567', '123', '12345678901', '12345']
    expected = '1234567'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 10:
    print()
    print('Test 10:')
    strings = ['123', '12345678901', '12345', '1234567']
    expected = '123'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 11:
    print()
    print('Test 11:')
    strings = ['12345678901', '12345', '1234567', '123']
    expected = '12345678901'
    actual = problem1d(strings)
    print('  This test case calls:')
    print('    problem1d(', strings, ')')
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)


def problem1d(strings):
    """
    What comes in:
      -- a sequence of strings
    What goes out:
      Returns the first string in the sequence whose length is prime.
      If no string in the sequence has a prime length, then this function
      returns -1. (Again, treat 0 and 1 as NOT prime.)
    Side effects: None.
    Examples:

      If the given sequence of strings is:
          ['1234', '1234567890', '123', '12', '1', '123', '123']
      then this function returns
          '123'
      since '123' is the first string whose length (3) is prime.

      If the given sequence of strings is:
          ['ab', '1234567890', '123', '12', '1', '123', '123']
      then this function returns
          'ab'
      since 'ab' is the first string whose length (2) is prime.

      If the given sequence of strings is:
          ['1234', '1234567890', '1234', '12345678', '1', '', '12345678901']
      then this function returns
          '12345678901'
      since '12345678901' is the first string whose length (11) is prime.

      If the given sequence of strings is:
          ['1234', '1234567890', '1234', '12345678', '1', '']
      then this function returns
          -1
      since there are no strings in the sequence whose length is prime.
    Type hints:
      :type strings: list of str
      :rtype: str | -1
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    for i in range(len(strings)):
        if is_prime(len(strings[i])) is True:
            return strings[i]

    else:
        return -1

###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_result_of_test(expected, actual):
    testing_helper.print_result_of_test(expected, actual)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
