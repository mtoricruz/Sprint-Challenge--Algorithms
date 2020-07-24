'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0

    # base case:
    if len(word) <= 1:
        return 0
    # check to see if index values are th lowercase
    if word[0] == 't' and word[1] == 'h':
        # if yes increment counter of th's in string
        counter += 1
    # then recursively move through the string to cycle through logic and return the counter total
    return count_th(word[1:]) + counter


