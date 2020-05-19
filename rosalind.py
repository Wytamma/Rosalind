import typer
from typing import List
from pathlib import Path
from python_village import ini3, ini4, ini5, ini6

def main(
    name_of_problem: str = typer.Argument(...), 
    path_to_dataset: Path = typer.Option(None, "--dataset", "-d", help="Path to dataset."),
    test: bool = typer.Option(False, "--test", "-t", help="Test the soultion.")
    ):
    try:
        problem = eval( name_of_problem )
    except NameError:
        typer.echo(typer.style(f"The problem with name: '{name_of_problem}' in not defined, you may have a typo or forgot to import it.", fg=typer.colors.WHITE, bg=typer.colors.RED))
        raise typer.Abort()
    if not path_to_dataset:
        output = problem.solution(problem.SAMPLE_DATASET)
        typer.echo(output)
        if test:
            try:
                assert output == problem.SAMPLE_OUTPUT
                typer.echo(typer.style('\nThe solution is correct!', fg=typer.colors.GREEN, bold=True))
            except:
                typer.echo(typer.style('\nThe soultion is not correct!', fg=typer.colors.RED, bold=True)) 
                typer.echo('Correct output:\n')
                typer.echo(problem.SAMPLE_OUTPUT)

    else:
        with open(path_to_dataset) as f:
            dataset_lines = f.readlines()
        typer.echo(problem.solution(dataset_lines))

if __name__ == "__main__":
    typer.run(main)