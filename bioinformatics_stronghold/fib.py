SAMPLE_DATASET = """5 3"""
SAMPLE_OUTPUT = """19"""


def population_size(n: int, k: int) -> int:
    """
    Returns the population at time 'n' given 'k' generation size.
    Fn = Fn−1 + (Fn−2 * k)
    """
    if n <= 2:
        # F1 = F2 = 1
        return 1
    return population_size(n - 1, k) + (population_size(n - 2, k) * k)


def solution(dataset: list) -> str:
    n, k = map(int, dataset[0].strip().split())
    return str(population_size(n, k))


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
