def rev_string(astring):
    """another way to reverse a string in place"""
    #strings are immutable(cannot change), must convert to a list
    string_list = list(astring) 
    i = 0

    #while the index is less than half the string bc we are rebinding the indexes
    while i < len(string_list)/2: 
        #swap 
        string_list[i], string_list[-(i+1)] = string_list[-(i+1)], string_list[i] 
        #increment the index
        i = i + 1
    #turn the list back into a string
    return "".join(string_list)

# print rev_string("hello")

###################################################################################################

def reverse(string):
    """reverse a string in place by interview cake"""
    #conver string to list
    string_list = list(string)

    #left position is initalized at 0
    left_position  = 0
    #right position is initialized at (len of list-1)
    right_position = len(string_list) - 1

    #while the left position is less than the right position
    while left_position < right_position:
        #take the item at the left position and put it into the temp variable (holding spot for the item)
        temp = string_list[left_position]
        #rebind the left position with the item at the right position (last to first)
        string_list[left_position]  = string_list[right_position]
        #rebind the right position with the item in the temp variable (item @left position)
        string_list[right_position] = temp

        left_position  += 1 #increment left position 
        right_position -= 1 #decrement right position (bc we going backwards) until while loop is false (middle)

    return ''.join(string_list)

#print reverse('hello')

###################################################################################################

def rev_string(astring):
    """reverse a string (not in place)"""
    
    r = ""
    #for each index in the range (list of numbers within) of the length of string (length is a single number)
    for i in range(len(astring)):
        #add items to r, staring at the last index 
        r = r + astring[-(i+1)]
    return r

# print rev_string("hello")
###################################################################################################
def repeat_char(number):
    """ Print the first repeating character
        Example: input: 123LK63824K output: 3"""

    new_list = []
    dupe_list = []
    
    for num in number:
      if num not in new_list:
        new_list.append(num)
      else:
        dupe_list.append(num)
    print dupe_list[0]     
          
# print repeat_char("123LK63824K")

###################################################################################################
def anagram(wordlist):
    """ An anagram is a word that is a valid rescrambling of another word. For example, cat is an anagram of act. 
        Find the word that has the most anagrams of any other word in that list."""

    mydict = {}

    for word in wordlist:
        #sort the word but sorting turns the word into a list of strings
        sorted_list = sorted(word)
        #turn it back into a string 
        sorted_word = "".join(sorted_list) 
        if sorted_word not in mydict:
            mydict[sorted_word] = []
            mydict[sorted_word].append(word)
        else:
            mydict[sorted_word].append(word)
    #returns a list of values
    return mydict.values()

# print anagram(['cat', 'dog', 'act', 'god', 'mouse'])


###################################################################################################
def palindrome(word): #kind of like reversing a string in place
    """ An palindrome is a word that is spelled the same backwards.
        Return True/False if this word is a palindrome.
        Example: racecar, noon """
    wlist = list(word)
    i = 0

    while i < len(word)/2:
        if wlist[i] == wlist[-(i+1)]:
            return True
        else:
            return False

# print palindrome("racecar")

###################################################################################################
def prime(n):
    """ A prime number is a number >= 2 that is only evenly divisible 
        by itself and 1. So, for example, 3 is a prime number but 4 (divisible by 2) 
        is not. The first few primes are: 2, 3, 5, 7, 11. Write a function that produces 
        count prime numbers, where count is a value passed into the function. """
    #less than 2 is false
    if n < 2:
        return False
    #at each index from range 2 to n, index is all the numbers that come before n (looks for factorial)
    for i in range(2, n):
        #if any number evenly divides,return false (not prime)
        if i % n == 0:
            return False
        else:
            return True
    
# print prime(5)

###################################################################################################
def swap_case(S):
    """ Convert all lower case letters to upper case and vice versa. """
    newlist = []
    for item in S:
        if item == item.upper():
            newlist.append(item.lower())
        elif item == item.lower():
            newlist.append(item.upper())
        else:
            newlist.append(item)
    return "".join(newlist)

# S = raw_input()
# print swap_case(S)
###################################################################################################
def sub_string(astring, substring):
    """print the number of times that substring occurs in that string"""
    match = 0
    #traverse the string by index; range is exclusive (up to but not including)
    for index in range(len(astring) - len(substring)+1):
        #slice the string by the len of the substring; slicing is exclusive
        #and check if it matches the substring
        if s[index : index + len(substring)] == substring:
            match += 1
    return match

print sub_string('ABCDCDC', 'CDC')
###################################################################################################
def fibonacci():
    """ adding two numbers together and print out the next number"""
    #initialize a and b
    a, b = 0, 1
    for i in range (0, 10):
        print a
        a,b = b, a+b
###################################################################################################
class Node(object):
    """ Implement a GetNth() function that takes a linked list and an integer 
        index and returns the node stored at the Nth index position. 
        GetNth() uses the C numbering convention that the first node is index 0, 
        the second is index 1, ... and so on. So for the list 42 -> 13 -> 666, GetNth() 
        with index 1 should return Node(13); The index should be in the range [0..length-1]. 
        If it is not, GetNth() should throw/raise an exception. 
        You should also raise an exception if the list is empty/null/None. """

    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
  if node is None or index < 0:
      raise Exception      
  for i in range(index):
      if node.next is None:
          raise Exception
      node = node.next
  return node

###################################################################################################

def encode(string):
    """#Takes in a string str and replaces all the letters with their 
    respective positions in the English alphabet."""
    mydict={}
    new=[]
    string = string.lower()
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    
    for i, letter in enumerate(alphabet, start=1):
        mydict[letter]= str(i)
    
    for char in string:
        if char not in mydict:
            new.append(char)
        else:
            new.append(mydict.get(char))
    return "".join(new)

###################################################################################################

#parenthesis match checker
def parChecker(symbolString):
    temp = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            temp.append(symbol)
        else:
            if temp == []:
                balanced = False
            else:
                temp.pop()
        index = index + 1
    if balanced and temp == []:
        return True
    else:
        return False
# print parChecker("((())")

###################################################################################################


def matches(opener, closer):
    open_braces = "([{"
    close_braces = ")]}"
    return open_braces.index(opener) == close_braces.index(closer)
# print matches("[", "}")

# def braces


