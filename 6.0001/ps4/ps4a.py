# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(s, i=0):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if isinstance(s, str):
        s = list(s)

    if i >= len(s) - 1:
        return ["".join(s)]
    permutations = get_permutations(s, i + 1)
    
    for j in range(i + 1, len(s)):
        s[i], s[j] = s[j], s[i]
        permutations.extend(get_permutations(s, i + 1))
        s[i], s[j] = s[j], s[i]
    return permutations

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('')
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example1 = 'rob'
    print('Input:', example1)
    print('Expected Output:', ['rob', 'rbo', 'orb', 'obr', 'bor', 'bro'])
    print('Actual Output:', get_permutations(example1))
    print('')
    example2 = 'tip'
    print('Input:', example2)
    print('Expected Output:', ['tip', 'tpi', 'itp', 'ipt', 'pit', 'pti'])
    print('Actual Output:', get_permutations(example2))
    print('')
    example3 = 'can'
    print('Input:', example3)
    print('Expected Output:', ['can', 'cna', 'acn', 'anc', 'nac', 'nca'])
    print('Actual Output:', get_permutations(example3))

    pass #delete this line and replace with your code here

