SAMPLE_DATASET = """HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102"""
SAMPLE_OUTPUT = "Humpty Dumpty"


def solution(dataset):
    words = dataset[0]
    indices = [int(indice) for indice in dataset[1].split()]
    word1 = words[indices[0] : indices[1] + 1]
    word2 = words[indices[2] : indices[3] + 1]
    return f"{word1} {word2}"
