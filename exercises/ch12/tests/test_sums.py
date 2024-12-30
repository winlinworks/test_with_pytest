# import sys
# import pytest
from subprocess import run
from typer.testing import CliRunner

import sums

# def test_sys_path():
#     print("sys.path: ")
#     for path in sys.path:
#         print(path)

runner = CliRunner()

def test_sums():
    result = run(["python", 'src/sums.py'], capture_output=True, text=True)
    output = result.stdout
    assert output == "200.00\n"


def test_sums_import(capsys):
    result = runner.invoke(sums.app).stdout
    assert result == "200.00\n"

def test_sums_import_file():
    result = runner.invoke(sums.app, ["src/data.txt"]).stdout
    assert result == "200.00\n"

# @pytest.mark.xfail
def test_sums_import_file_not_200(capsys):
    result = runner.invoke(sums.app, ["src/data_not_200.txt"]).stdout
    assert result != "200.00\n"

