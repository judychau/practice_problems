def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    odd_list = []
    for i in number_list:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

    #list comprehension
    # return [d for d in number_list if d % 2 != 0]

# number_list = [1, 2, 7, -5]
# print all_odd(number_list) 

###################################################################################################
def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_list = []
    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

    #list comprehension
    # return [d for d in number_list if d % 2 == 0]

# number_list = [2, 6, -1, -2]
# print all_even(number_list) 

###################################################################################################
def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """
    for i in range(len(my_list)):
            print i, my_list[i]

    ####OR###

    # i = 0 
    # while i < len(my_list):
    #     print i, my_list[i]
    #     i+= 1

# my_list = ["Toyota", "Jeep", "Volvo"]
# print print_indeces(my_list)
###################################################################################################
def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_list = []
    for word in word_list:
        if len(word) > 4:
            long_list.append(word)
    return long_list

    #list comprehension
    # return [w for w in word_list if len(w) > 4]

# print long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])

###################################################################################################
def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    smallest = None
    for num in number_list:
        if smallest is None or num < smallest:
            smallest = num
    return smallest

# print smallest_int([-5, 2, -5, 7])

###################################################################################################
def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    largest = None
    for num in number_list:
        if largest is None or num > largest:
            largest = num
    return largest
    
# print largest_int([-5, 2, -5, 7])
###################################################################################################
def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    halflist = []
    for num in number_list:
        halflist.append(num/2.0)
    return halflist

    #list comprehension
    #return [i / 2.0 for i in number_list]

# print halvesies([2, 6, -2, 5])

###################################################################################################
def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    length_list = []
    for word in word_list:
        length_list.append(len(word))
    return length_list

    #list comprehension
    # return [len(word) for word in word_list]

# print word_lengths(["hello", "hey", "hello", "spam"])
###################################################################################################
def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0
    for num in number_list:
        total += num
    return total

# print sum_numbers([1, 2, 3, 10])

###################################################################################################
def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    total = 1
    for num in number_list:
        total *= num
    return total

# print mult_numbers([1, 2, 3])

###################################################################################################
def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    new_string = ""
    for word in word_list:
        new_string += word
    return new_string

# print join_strings(["spam", "spam", "bacon", "balloonicorn"])
###################################################################################################
def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    total = 0
    for num in number_list:
        total += num
    return total/float(len(number_list))

    ###OR##

    # total = sum(number_list)
    # return total/float(len(number_list))

# print average([2, 12, 3])

###################################################################################################
def intermediate_join_strings(list_of_words):
    """Return a single string with each word from the input list
    separated by a comma.

    Do this with a list comprehension. See
    https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
    for more info.

    >>> intermediate_join_strings(["Labrador", "Poodle", "French Bulldog"])
    'Labrador, Poodle, French Bulldog'

    As above, if the list given is empty, it's fine if this function
    raises an error.
    """
    return ", ".join(list_of_words)

    ###OR###

    # output = list_of_words[0]
    # for word in list_of_words[1:]:
    #     output = output + ", " + word
    # return output

# print intermediate_join_strings(["Labrador", "Poodle", "French Bulldog"])
###################################################################################################
def adv_find_unique_long_words(my_string):
    """Return a list of words that only appeared only once
    within the input string and are at least 6 characters long.

    >>> adv_find_unique_long_words("I ate popcorn, more popcorn, nachos, kale, and coffee.")
    ['nachos', 'coffee']

    """
    unique = []
    punctuation=['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]

    for char in my_string:
        if char in punctuation:
            my_string = my_string.replace(char, "")
            string_list = my_string.split()

    for word in string_list:
        if len(word)>=6 and string_list.count(word) == 1:
            unique.append(word)
    return unique

# print adv_find_unique_long_words("I ate popcorn, more popcorn, nachos, kale, and coffee.")

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print