SAMPLE_DATASET = """100 200""".splitlines(True)
SAMPLE_OUTPUT = "7500"

def solution(dataset):
    numbers = dataset[0].split()
    first = int(numbers[0])
    last= int(numbers[1])
    return str(sum([i for i in range(first, last+1) if i % 2 != 0]))
    



