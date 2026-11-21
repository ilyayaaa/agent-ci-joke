import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, "main.py")


def run(cwd):
    with tempfile.TemporaryDirectory() as out:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out)
        r = subprocess.run([sys.executable, MAIN], cwd=cwd, env=env)
        assert r.returncode == 0, f"exit {r.returncode} in {cwd}"
        with open(os.path.join(out, "entry.txt"), "rb") as f:
            return f.read()


def main():
    a = run("/")
    b = run(tempfile.gettempdir())
    assert a == b, "outputs differ"
    text = a.decode("utf-8")
    assert 1 <= len(text) <= 280, "bad length"
    assert text.strip(), "only whitespace"
    print("ok")
    print(text)


if __name__ == "__main__":
    main()
