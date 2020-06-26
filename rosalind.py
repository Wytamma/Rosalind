import typer
from pathlib import Path

from python_village import ini3, ini4, ini5, ini6
from bioinformatics_stronghold import (
    dna,
    rna,
    revc,
    hamm,
    fib,
    gc,
    iprb,
    prot,
    subs,
    cons,
    fibd,
    grph,
    iev,
    lcsm,
)


def main(
    name_of_problem: str = typer.Argument(...),
    path_to_dataset: Path = typer.Option(
        None, "--dataset", "-d", help="Path to dataset."
    ),
    test: bool = typer.Option(False, "--test", "-t", help="Test the soultion."),
):
    try:
        problem = globals()[name_of_problem]
    except KeyError:
        typer.echo(
            typer.style(
                f"The problem '{name_of_problem}' is not defined, you may have a typo or forgot to import it.",
                fg=typer.colors.WHITE,
                bg=typer.colors.RED,
            )
        )
        raise typer.Abort()

    if path_to_dataset:
        with open(path_to_dataset) as f:
            dataset_lines = f.readlines()
        return typer.echo(problem.solution(dataset_lines))

    output = problem.solution(problem.SAMPLE_DATASET.splitlines(True))

    if test:
        try:
            assert output == problem.SAMPLE_OUTPUT
            return typer.echo(
                typer.style(
                    "The solution is correct!", fg=typer.colors.GREEN, bold=True
                )
            )
        except AssertionError:
            typer.echo(
                typer.style(
                    "The soultion is not correct!", fg=typer.colors.RED, bold=True
                )
            )
            typer.echo("Correct output:")
            typer.echo(problem.SAMPLE_OUTPUT)
            typer.echo("Current output:")

    return typer.echo(output)


if __name__ == "__main__":
    typer.run(main)
