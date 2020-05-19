import typer
from typing import List
from pathlib import Path
from python_village import ini3, ini4, ini5, ini6

def main(
    problem: str = typer.Argument(...), 
    dataset: Path = typer.Option(None, "--dataset", "-d", help="Path to dataset."),
    test: bool = typer.Option(False, "--test", "-t", help="Test the soultion.")
    ):
    try:
        problem = eval( problem )
    except NameError:
        typer.echo(f"The problem with name: '{problem}' in not defined, you may have a typo or forgot to import it.")
        raise typer.Abort()
    if not dataset:
        output = problem.solution(problem.SAMPLE_DATASET)
        typer.echo(output)
        if test:
            try:
                assert output == problem.SAMPLE_OUTPUT
                typer.echo('The solution is correct!')
            except:
                typer.echo('The soultion is not correct!\n') 
                typer.echo(f'Correct output: {problem.SAMPLE_OUTPUT}')
    else:
        with open(dataset) as f:
            dataset_lines = f.readlines()
        typer.echo(problem.solution(dataset_lines))

if __name__ == "__main__":
    typer.run(main)