import typer
import problems
from pathlib import Path

app = typer.Typer()

@app.command()
def test(name: str):
    getattr(problems, name).test()

@app.command()
def compute(name: str, dataset_path: Path):
    with open(dataset_path) as f:
        dataset = f.readlines()
    print(getattr(problems, name).solution(dataset))

if __name__ == "__main__":
    app()
