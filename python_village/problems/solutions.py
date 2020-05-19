def ini3_solution(dataset):
    """
    Given: A string s of length at most 200 letters and four integers a, b, c and d.
    Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
    """
    words = dataset[0]
    indices = [int(indice) for indice in dataset[1].split()] 
    word1 = words[indices[0]:indices[1]+1]
    word2 = words[indices[2]:indices[3]+1]
    return f"{word1} {word2}"

def ini4_solution(dataset):
    """
    Given: Two positive integers a and b (a<b<10000).
    Return: The sum of all odd integers from a through b, inclusively.
    """
    numbers = dataset[0].split()
    first = int(numbers[0])
    last= int(numbers[1])
    return str(sum([i for i in range(first, last+1) if i % 2 != 0]))

def ini5_solution(dataset):
    """
    Reading and Writingclick to expand
    
    Problem
    Given: A file containing at most 1000 lines.
    Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

    Sample Dataset
    Bravely bold Sir Robin rode forth from Camelot
    Yes, brave Sir Robin turned about
    He was not afraid to die, O brave Sir Robin
    And gallantly he chickened out
    He was not at all afraid to be killed in nasty ways
    Bravely talking to his feet
    Brave, brave, brave, brave Sir Robin
    He beat a very brave retreat
    
    Sample Output
    Yes, brave Sir Robin turned about
    And gallantly he chickened out
    Bravely talking to his feet
    He beat a very brave retreat
    """
    return "".join([line for i, line in enumerate(dataset, 1) if i % 2 == 0])


def ini6_solution(dataset):
    """
    Intro to Python dictionaryclick to expand
    
    Problem
    Given: A string s of length at most 10000 letters.
    Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

    Sample Dataset
    We tried list and we tried dicts also we tried Zen
    
    Sample Output
    and 1
    We 1
    tried 3
    dicts 1
    list 1
    we 2
    also 1
    Zen 1
    """
    from collections import Counter
    words = dataset[0].split()
    c = Counter(words)
    return "\n".join([f"{word} {c[word]}" for word in c])