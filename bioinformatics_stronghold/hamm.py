SAMPLE_DATASET = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""
SAMPLE_OUTPUT = 7

def solution(dataset: list) -> str:
    """"there is a '\n' on the end of the first line but zip() will only go to the sortest length.
    If both lines have '\n's then they will be equivalent and won't be counted"""
    return sum(i != j for i, j in zip(*dataset)) 
