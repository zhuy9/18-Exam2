"""
Exam 2, problem 3.

This module contains:
  -- Methods you must implement for the Cloud object
  
Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and YUCHEN ZHU  October 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
from numbers import Number
import testing_helper


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

    run_test_init()
    run_test_rain()
    run_test_get_total_rain_amount()
    run_test_merge_cloud()


###############################################################################
# The   Cloud   class (and its methods) begins here.
###############################################################################

class Cloud(object):
    """
    A Cloud has:
        -- capacity, a number representing the maximum amount of water
             that this Cloud can hold
        -- water, a number representing the amount of water this Cloud
             currently holds
    """

    def __init__(self, capacity, water):
        """
        What comes in:
          -- capacity, a number representing the maximum amount of water
               that this Cloud can hold
          -- water, a number representing the amount of water this Cloud
               currently holds
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Stores the Cloud's capacity and water in instance variables:
                  self.capacity
                  self.water
          -- If water is GREATER than capacity,
             then set   self.water   to be equal to   self.capacity.
                  (i.e.., A Cloud cannot hold more water than its capacity
                  even if a caller attempts to construct such a cloud).
          -- Initializes other instance variables as needed by methods
        Examples:
          cloud1 = Cloud(10, 3)
            #   cloud1.capacity  is now 10
            #   cloud1.water     is now 3
 s
          cloud2 = Cloud(10, 35)
            #   cloud2.capacity  is now 10
            #   cloud2.water     is now 10
            # Notice that the water is capped to the max capacity in this case

        Type hints:
          :type capacity: int | float
          :type water: int | float
        """
        # ---------------------------------------------------------------------
        # DONE: 2. Implement and test this method.
        # ---------------------------------------------------------------------
        self.capacity = capacity
        if water <= capacity:
            self.water = water
        else:
            self.water = capacity
        self.count = 0

    def rain(self, rain_amount):
        """
        What comes in:
          -- self
          -- a number   rain_amount   that specifies how much it "rains",
               that is, how much this Cloud's  water  should be reduced by,
               subject to the constraint that this Cloud's  water  cannot
               become negative.  That is, if the  rain_amount  is greater than
               this Cloud's current  water, then it "rains" only the amount
               of  water  that the Cloud currently holds. (See examples below.)
        What goes out:
          -- the amount of water that left the cloud
               (Note: this will be the same as  rain_amount  unless
               rain_amount   exceeds this Cloud's current water, in which
               case it will be this Cloud's current water.)

        Side effects:  Reduces the amount of water held in this cloud as appropriate.

        Examples:
          cloud1 = Cloud(10, 8)
          rain_amount = cloud1.rain(5)
            #   cloud1.capacity   is still 10
            #   cloud1.water      is now 3
            #   rain_amount       is 5

          cloud2 = Cloud(10, 2)
          rain_amount = cloud2.rain(35)
            #   cloud2.capacity   is still 10
            #   cloud2.water      is now 0
            #   rain_amount       is 2 (since cloud2 had only 2 water to give)

          cloud3 = Cloud(10, 50)
            #   cloud3.capacity   is 10
            #   cloud3.water      is 10 (not 50)
          rain_amount = cloud3.rain(60)
            #   cloud3.capacity   is still 10
            #   cloud3.water      is now 0
            #   rain_amount       is 10 (since cloud3 had only 10 water to give)
        Type hints:
          :type  rain_amount: int | float
          :rtype: int | float
        """
        # ---------------------------------------------------------------------
        # DONE: 3. Implement and test this method.
        # ---------------------------------------------------------------------
        if rain_amount <= self.water:
            self.water -= rain_amount
            self.count += rain_amount  # get total rain amount
            return rain_amount
        else:
            rain_amt = self.water
            self.water = 0
            self.count += rain_amt  # get total rain amount
            return rain_amt


    def get_total_rain_amount(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns the total amount of water that has been rained
               out of this Cloud.
        Side effects:
          -- None
        Examples:
          cloud1 = Cloud(10, 8)
          cloud1.rain(5)
          cloud1.rain(2)
          total_rain_amount = cloud1.get_total_rain_amount()
            #   cloud1.capacity   is still 10
            #   cloud1.water      is now 1
            #   total_rain_amount is 7

          cloud2 = Cloud(10, 2)
          cloud2.rain(35)
          cloud2.rain(1)
          total_rain_amount = cloud2.get_total_rain_amount()
            #   cloud2.capacity   is still 10
            #   cloud2.water      is now 0
            #   total_rain_amount is 2

        Type hints:
          :rtype: int | float
        """
        # ---------------------------------------------------------------------
        # DONE: 4. Implement and test this method.
        # ---------------------------------------------------------------------
        return self.count

    def merge_cloud(self, another_cloud):
        """
        What comes in:
          -- self
          -- another_cloud is a different Cloud object
        What goes out:
          -- Nothing (i.e. None)
        Side effects:
          -- The water from  another_cloud  is added to this cloud's water.
          -- The capacity of  another_cloud  is added to this cloud's capacity.
          -- The water and capacity  of another_cloud   are set to 0.
        Examples:
          cloud1 = Cloud(10, 3)
          cloud2 = Cloud(10, 5)
          cloud1.merge_cloud(cloud2)
            #   cloud1.capacity   is 20
            #   cloud1.water      is 8
            #   cloud2.capacity   is 0
            #   cloud2.water      is 0          

          cloud3 = Cloud(10, 100)
          cloud4 = Cloud(100, 0)
          cloud4.merge_cloud(cloud3)
            #   cloud3.capacity   is 0
            #   cloud3.water      is 0
            #   cloud4.capacity   is 110
            #   cloud4.water      is 10
        """
        # ---------------------------------------------------------------------
        # DONE: 5. Implement and test this method.
        # ---------------------------------------------------------------------
        self.capacity += another_cloud.capacity
        self.water += another_cloud.water
        another_cloud.capacity = 0
        another_cloud.water = 0
###############################################################################
# The TEST functions for the  Cloud  class begin here.
###############################################################################

def run_test_init():
    """ Tests the   __init__   method of the Cloud class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Cloud class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    cloud1 = Cloud(10, 3)
    expected_capacity = 10
    expected_water = 3
    run_test_instance_variables(cloud1, expected_capacity, expected_water)

    # Test 2
    print('\nTest 2:')
    cloud2 = Cloud(10, 35)
    expected_capacity = 10
    expected_water = 10
    run_test_instance_variables(cloud2, expected_capacity, expected_water)


def run_test_rain():
    """ Tests the   rain   method of the Cloud class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   rain   method of the Cloud class.')
    print('-----------------------------------------------------------')

    # Test 1:
    print('\nTest 1:')
    cloud1 = Cloud(10, 8)
    rain_amount = cloud1.rain(5)
    print('  Testing the return value:')
    expected = 5
    actual = rain_amount
    print("    Expected:", expected)
    print("    Actual:  ", actual)
    print_result_of_test(expected, actual)
    print()
    run_test_instance_variables(cloud1, 10, 3)

    # Test 2:
    print('\nTest 2:')
    cloud2 = Cloud(10, 2)
    rain_amount = cloud2.rain(35)
    #   cloud2.capacity   is still 10
    #   cloud2.water      is now 0
    #   rain_amount       is 2 (since cloud2 had only 2 water to give)
    print('  Testing the return value:')
    expected = 2
    actual = rain_amount
    print("    Expected:", expected)
    print("    Actual:  ", actual)
    print_result_of_test(expected, actual)
    print()
    run_test_instance_variables(cloud2, 10, 0)

    # Test 3:
    print('\nTest 3:')
    cloud3 = Cloud(10, 50)
    rain_amount = cloud3.rain(60)
    #   cloud3.capacity   is still 10
    #   cloud3.water      is now 0
    #   rain_amount       is 10 (since cloud3 had only 10 water to give)
    print('  Testing the return value:')
    expected = 10
    actual = rain_amount
    print("    Expected:", expected)
    print("    Actual:  ", actual)
    print_result_of_test(expected, actual)
    print()
    run_test_instance_variables(cloud3, 10, 0)


def run_test_get_total_rain_amount():
    """ Tests the   get_total_rain_amount   method of the Cloud class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_total_rain_amount   method of the Cloud class.')
    print('-----------------------------------------------------------')

    # Test 1:
    print('\nTest 1:')
    cloud1 = Cloud(10, 8)
    cloud1.rain(5)
    cloud1.rain(2)
    total_rain_amount = cloud1.get_total_rain_amount()
    #   cloud1.capacity   is still 10
    #   cloud1.water      is now 1
    #   total_rain_amount is 7
    print('  Testing the return value:')
    expected = 7
    actual = total_rain_amount
    print("    Expected:", expected)
    print("    Actual:  ", actual)
    print_result_of_test(expected, actual)
    print()
    run_test_instance_variables(cloud1, 10, 1)

    # Test 2:
    print('\nTest 2:')
    cloud2 = Cloud(10, 2)
    cloud2.rain(35)
    cloud2.rain(1)
    total_rain_amount = cloud2.get_total_rain_amount()
    #   cloud2.capacity   is still 10
    #   cloud2.water      is now 0
    #   total_rain_amount is 2
    print('  Testing the return value:')
    expected = 2
    actual = total_rain_amount
    print("    Expected:", expected)
    print("    Actual:  ", actual)
    print_result_of_test(expected, actual)
    print()
    run_test_instance_variables(cloud2, 10, 0)


def run_test_merge_cloud():
    """ Tests the   merge_cloud   method of the Cloud class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   merge_cloud   method of the Cloud class.')
    print('-----------------------------------------------------------')

    # Test 1:
    print('\nTest 1:')
    cloud1 = Cloud(10, 3)
    cloud2 = Cloud(10, 5)
    cloud1.merge_cloud(cloud2)
    #   cloud1.capacity   is 20
    #   cloud1.water      is 8
    #   cloud2.capacity   is 0
    #   cloud2.water      is 0
    run_test_instance_variables(cloud1, 20, 8)
    run_test_instance_variables(cloud2, 0, 0)

    # Test 2:
    print('\nTest 2:')
    cloud3 = Cloud(10, 100)
    cloud4 = Cloud(100, 0)
    cloud4.merge_cloud(cloud3)
    #   cloud3.capacity   is 0
    #   cloud3.water      is 0
    #   cloud4.capacity   is 110
    #   cloud4.water      is 10
    run_test_instance_variables(cloud3, 0, 0)
    run_test_instance_variables(cloud4, 110, 10)


###############################################################################
# The following are HELPER functions that display error messages in RED
# and help make it easier for us to write tests.
# Do NOT change any of the following.
###############################################################################


def run_test_instance_variables(cloud, expected_capacity, expected_water):
    """
    Tests whether the instance variables for the given Cloud are per the given expected values.
      -- Prints relevant messages.
      -- Returns True if all is OK, else returns False.
    """
    try:
        return (run_test_type_of_object(cloud) and
                run_test_types_of_instance_variables(cloud) and
                run_test_values_of_instance_variables(
                    cloud,
                    expected_capacity,
                    expected_water))
    except Exception:
        something_unexpected_happened_in_our_testing_code()
        return False


def run_test_values_of_instance_variables(cloud, expected_capacity, expected_water):
    # Print the EXPECTED and ACTUAL values of the instance variables
    format_string = '  {:9} {:7}       {}'
    print('  Testing instance variables:')
    print('              capacity   water')
    print('              --------   -----')
    print(format_string.format('Expected:', expected_capacity, expected_water))
    print(format_string.format('Actual:', cloud.capacity, cloud.water))

    # Print a message indicating whether or not
    # the EXPECTED values are equal to the ACTUAL values.
    expected = (expected_capacity, expected_water)
    actual = (cloud.capacity, cloud.water)
    return print_result_of_test(expected, actual)


def something_unexpected_happened_in_our_testing_code():
    print_failure_message()
    explanation = (
        '  Something unexpected has happened in the testing \n' +
        '  code that we supplied.  You should probably\n' +
        '  SEEK HELP FROM YOUR INSTRUCTOR NOW.')
    print_failure_message(explanation)


def run_test_type_of_object(cloud):
    """ Returns True if the argument is in fact a Cloud object """
    if isinstance(cloud, Cloud):
        return True
    else:
        explanation = ('  The following object to test:\n' +
                       '     ' + str(cloud) + '\n' +
                       '  should be a Cloud object,\n' +
                       '  but it is not.  Perhaps your code\n' +
                       '  returned something of the wrong type?')
        print_failure_message()
        print_failure_message(explanation)
        return False


def run_test_types_of_instance_variables(cloud):
    """
    Returns True if the argument has the right instance variables
    and they are all numbers.
    """
    # If NONE of the expected instance variables exist,
    # then perhaps the only "problem" is that the  __init__  method
    # has not yet been implemented.
    attributes = dir(cloud)
    if ('capacity' not in attributes
            and 'water' not in attributes):
        explanation = (
            '  This object:\n' +
            '     ' + str(cloud) + '\n' +
            '  should have these instance variables:\n' +
            '     capacity\n' +
            '     water\n' +
            '  but it has NONE of them.\n' +
            '  Perhaps you simply have not yet\n' +
            '  implemented the   __init__   method?\n' +
            '  (If so, implement it now.)')
        print_failure_message()
        print_failure_message(explanation)
        return False

    # If SOME (but not all) of the expected instance variables exist,
    # then perhaps something was misspelled in __init__.
    if not ('capacity' in attributes
            and 'water' in attributes):
        explanation = (
            '  This object:\n' +
            '     ' + str(cloud) + '\n' +
            '  should have these instance variables:\n' +
            '     capacity\n' +
            '     water\n' +
            '  but it is missing some of them.\n' +
            '  Perhaps you misspelled something\n' +
            '  in your   __init__   code?')
        print_failure_message()
        print_failure_message(explanation)
        return False

    # Check that the instance variables are of the right types:
#     if not isinstance(cloud.capacity, str):
#         explanation = (
#             '  This object:\n' +
#             '     ' + str(cloud) + '\n' +
#             '  has an instance variable  capacity  with this value:\n' +
#             '     capacity: ' + str(cloud.capacity) +
#             '  That value should be a STRING, but is isn\'t.\n')
#         print_failure_message()
#         print_failure_message(explanation)
#         return False
#
#     if not isinstance(cloud.water, list):
#         explanation = (
#             '  This object:\n' +
#             '     ' + str(cloud) + '\n' +
#             '  has an instance variable  water  with this value:\n' +
#             '     water: ' + str(cloud.water) +
#             '  That value should be a LIST, but is isn\'t.\n')
#         print_failure_message()
#         print_failure_message(explanation)
#         return False
#
#     if not is_list_of_strings(cloud.water):
#         explanation = (
#             '  This object:\n' +
#             '     ' + str(cloud) + '\n' +
#             '  has an instance variable  water  with this value:\n' +
#             '     water: ' + str(cloud.water) +
#             '  That value should be a list of STRINGS, but is isn\'t.\n')
#         print_failure_message()
#         print_failure_message(explanation)
#         return False

    return True


def is_list_of_strings(strings):
    return ((strings == [])
            or (isinstance(strings[0], str)
                and is_list_of_strings(strings[1:])))


def print_result_of_test(expected, actual):
    if are_equal(expected, actual):
        print("  PASSED the above test -- good!", color="blue")
        return True

    print_failure_message()

    if isinstance(expected, list) or isinstance(expected, tuple):
        explanation = (
            '  For at least one of the above, its Expected value\n' +
            '  does not equal its Actual value.')
#          Note: the printed\n' +
#             '  values are the actual values ROUNDED to 1 decimal place.')
        print_failure_message(explanation)

    return False


def are_equal(a, b):
    # We will treat two numbers as being "equal" if they are
    # the same when each is rounded to 12 decimal places.
    if isinstance(a, Number) and isinstance(b, Number):
        return (round(a, 12) == round(b, 12))

    # For lists and tuples, their items have to be equal for the
    # lists/tuples to be equal.
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    # For all else, they must be equal in the "usual" way:
    return a == b


def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=0.5):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message, flush=True, color="red")
    time.sleep(flush_time)


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
