from hello_world import hello

def test_hello_no_fixtures():
    hello()
    with open("hello.txt") as f:
        assert f.read() == "Hello World!\n"

def test_hello_fixtures(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    # print(tmp_path)
    hello()
    with open("hello.txt") as f:
        assert f.read() == "Hello World!\n"
