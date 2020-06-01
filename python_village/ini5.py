SAMPLE_DATASET = """Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat"""
SAMPLE_OUTPUT = """Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat"""


def solution(dataset):
    return "".join([line for i, line in enumerate(dataset, 1) if i % 2 == 0])
