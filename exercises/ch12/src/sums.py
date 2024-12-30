# sums.py
# add the numbers in `data.txt`
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def main(file_name: Optional[str] = typer.Argument("src/data.txt")):
    sum = 0.0

    # Open data.txt using the absolute path
    with open(file_name, "r") as file:
        for line in file:
            number = float(line)
            sum += number

    print(f"{sum:.2f}")

if __name__ == "__main__":
    app()