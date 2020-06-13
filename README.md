# Rosalind solutions
My solutions to the problems found on [rosalind.info](http://rosalind.info/problems/locations/)

## Solution template

```python
SAMPLE_DATASET = """"""
SAMPLE_OUTPUT = """"""

def solution(dataset: list) -> str:
    pass

def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
```

## CLI 

The file `rosalind.py` contains a cli that can be used to run and test solutions. 

### Testing
```bash
$ python rosalind.py NAME_OF_PROBLEM --test
```
### Running
```bash
$ python rosalind.py NAME_OF_PROBLEM --dataset PATH_TO_DATASET
```

