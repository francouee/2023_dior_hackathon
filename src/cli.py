import logging

import typer
from rich.console import Console


logging.basicConfig(level=logging.INFO)
cli = typer.Typer()
console = Console()

@cli.command("dataset", help="Build dataset")
def dataset(date: str = None) -> None:
    console.rule(f"[blue]{dataset.__name__}")


if __name__ == "__main__":
    cli()
