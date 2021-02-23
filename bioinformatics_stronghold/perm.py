SAMPLE_DATASET = """3"""
SAMPLE_OUTPUT = """6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1"""

def get_perms(array: list):
    """
    python implementation of Heap's algorithm
    """
    output = []
    def generate(k:int, A: list):
        if k == 1:
            return output.append(A.copy()) 
        generate(k-1, A)
        for i in range(k-1):
            if k % 2 == 0:
                A[i],A[k-1] = A[k-1],A[i]
            else:
                A[0],A[k-1] = A[k-1],A[0]
            generate(k-1, A)
            
    generate(len(array), array)
    return output

def solution(dataset: int) -> str:
    k = int(dataset[0])
    perumations = get_perms([str(i+1) for i in range(k)])
    return f"{len(perumations)}\n" + "\n".join([" ".join(p) for p in sorted(perumations)])

def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT