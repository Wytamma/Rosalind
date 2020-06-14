SAMPLE_DATASET = """6 3"""
SAMPLE_OUTPUT = 4


def slow_solution(dataset: list) -> str:
    population = []
    n, m = map(int, dataset[0].split())
    rabbit_pair_age = 0
    population.append(rabbit_pair_age)
    for _ in range(n):
        # breed
        for r in reversed(population):  # appending to array I'm looping through
            if r > rabbit_pair_age + 1:
                population.append(rabbit_pair_age)
        # age
        population = [r + 1 for r in population]
        # check who is alive
        population = [r for r in population if r <= m]
    return len(population)


import functools


def memorize(f):
    d = {}

    def helper(*args):
        if str(args) not in d:
            d[str(args)] = f(*args)
        return d[str(args)]

    return helper


@memorize
def population_size(n: int, m: int) -> int:
    if n < 0:
        return 0
    if n <= 2:
        return 1
    return sum([population_size(n - i, m) for i in range(2, m + 1)])


def solution(dataset: list) -> int:
    n, m = map(int, dataset[0].split())
    return population_size(n, m)


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
    assert slow_solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
    assert solution(["75 21"]) == 2109333161649033
