SAMPLE_DATASET = """2 2 2"""
SAMPLE_OUTPUT = 0.78333


def probably_of_dominate(mother_genotype, father_genotype):
    return sum([any((i, j)) for i in mother_genotype for j in father_genotype]) / len(
        mother_genotype + father_genotype
    )


def solution(dataset: list) -> float:
    genotypes = {"k": [1, 1], "m": [1, 0], "n": [0, 0]}
    genotypes_counts = dict(
        (org, int(pop)) for org, pop in zip(("k", "m", "n"), dataset[0].strip().split())
    )
    total_probability = 0

    for mother in genotypes:
        counts = genotypes_counts.copy()
        total = sum(counts.values())
        mc = counts[mother]
        counts[mother] -= 1
        for father in genotypes:
            fc = counts[father]
            total_probability += (
                (mc / total) * (fc / (total - 1))
            ) * probably_of_dominate(genotypes[mother], genotypes[father])

    return round(total_probability, 5)

def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT