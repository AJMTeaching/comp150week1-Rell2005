# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.

def my_list(): 
 my_list(1 , 5, 'apple', 20.5)
 print('apple')
 my_list.append(10)
 print(my_list)
 my_list.remove(20.5)
 print(my_list)
 my_list.reverse
 print(my_list)

# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.

 def dict(keys):(get_items)
 
 keys =["name" , "age", "job"]
 get_items = ("john", "30", "teacher")
 print('job')
 dict.appendkeys('city')
 dict.apppendget_items('paris')
 print[keys : get_items]
 dict.removekey("age")
 dict.removeget_items("30")
 print[ keys : get_items]
 keys == get_items
 print('name')
 print('job')
 print('city')
 print('john')
 print('teacher')
 print('paris')


# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    vowels = {
        'a',
        'e',
        'i',
        'o',
        'u',
        'A',
        'E',
        'I',
        'O',
        'U',
    }
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
 
    return count

    # TODO: Implement this function
    pass


# Unit Tests for count_vowels

def test_count_vowels():
    test(count_vowels("a") == 1)
    test(count_vowels("e") == 2)
    test(count_vowels("i")==3)
    test(count_vowels("o")==4)
    test(count_vowels("u")==5)
    test(count_vowels("y")==0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("A") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)

def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
list1 = [1,3,5]; list2 = [2,4,6]
merged = merge_lists(list1 , str(list2))

print(merged)


# TODO: Implement this function
pass
list1 = [1, 2, 5, 8, 10]; list2 = [3, 6, 7, 9, 11] 
merged = merge_lists(list1, str(list2))
print(merged)

  

# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], [4]) == [1, 3, 4, 5])
    test(merge_lists([1], [2, 4, 6]) == [1, 2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
words = [
    'I',
    'Am',
    'Turtle',
    'grass'
]
num = 0 
for num in words: 
    count_num =+ 1
    print(count_num)
 

    # TODO: Implement this function
    pass

def test_word_lengths():
    words = ["Hey", "My", "python", "world", "word"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths(["My"]) == [2])
    test(word_lengths(["Hey"]) == [3])
    test(word_lengths(["python"]) == [6])
    test(word_lengths(["world"]) == [5])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])

# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
def reverse_string(s):
 
 text_string = 'growth' 

 return s[ ::-1 ]

 print(reverse_string)


 # TODO: Implement this function
pass


def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa!") == "!aaa")
    test(reverse_string("goodbye, World!") == "!dlroW ,eybdoog")
    test(reverse_string("7711") == "1177")
    test(reverse_string("  taste  ") == "  etsat  ")

# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """

def intersection(a , b):
    a = [1,2,10,21,30,4,4]
    b =[1,4,4,88,21,36]

    res =  list(set(a) & set(b))

    print(res)

    # TODO: Implement this function
    pass


def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result ==  [])
    test(intersection([], []) == [])
    test(intersection([1], [1]) == [1])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([5, 2, 3], [4, 5, 6]) == [5])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])

# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
