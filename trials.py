"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array."""
    # pass  # TODO: replace this line with your code
    for item in items:
        print(item)

def get_all_evens(nums):
    """collect all even numbers"""
    # pass  # TODO: replace this line with your code
    even_nums = []
    for item in nums:
        if item % 2 == 0:
            even_nums.append(item)
    return even_nums


def get_odd_indices(items):
    """ just even items """
    # pass  # TODO: replace this line with your code
    return items[1::2]


def print_as_numbered_list(items):
    """Given a list, output a numbered list."""
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i += 1

def get_range(start, stop):
    """ a range of numbers by start and stop """
    # pass  # TODO: replace this line with your code
    nums = []
    for i in range(start, stop):
        nums.append(i)

def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'"""
    chars = []
    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    return "".join(chars)


def snake_to_camel(string):
    # pass  # TODO: replace this line with your code
    camelCase = []
    for word in string.split('_'):
        camelCase.append(f'{word[0].upper()}{word[1:]}')
    
    return "".join(camelCase)


def longest_word_length(words):
    """Return the length of the longest word in the given list of words."""
    longest=len(words[0])
    for word in words:
        if longest < len(word):
            longest=len(word)
    return longest


def truncate(string):
    # pass  # TODO: replace this line with your code
    result = []
    for letter in string:
        if len(result) == 0 or letter != result[len(result) - 1]:
            result.append(letter)

    return "".join(result)

def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced"""
    i=0
    for letter in string:
        if letter == '(':
            i +=1
        elif letter == ')':
            i -=1
            if i < 0:
                return False
    return i==0



def compress(string):
    """compress the string to include number"""
    
    compressed = []
    curr_char = ''
    char_count = 0
    for letter in string:
        if letter != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = letter
            char_count = 0

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)

# comp = compress("aaabc")
# print(comp)