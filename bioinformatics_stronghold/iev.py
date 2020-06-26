SAMPLE_DATASET = """1 0 0 1 0 1"""
SAMPLE_OUTPUT = 3.5

probabolites_of_dominate = [
    1,  # AA-AA
    1,  # AA-Aa
    1,  # AA-aa
    3 / 4,  # Aa-Aa
    2 / 4,  # Aa-aa
    0,  # aa-aa
]


def solution(dataset: list) -> float:
    n_of_couples_in_population = dataset[0].strip()
    return sum(
        int(n_of_couples) * probabolites_of_dominate[i] * 2
        for i, n_of_couples in enumerate(n_of_couples_in_population.split())
    )


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
