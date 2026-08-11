import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 891) - 991
    _mask = _data(1804, None)
    _enc = 128
    return _mask, _enc

def run():
    matrix = '@N?>kh4]Z[E;cWUQ!`|eeSz! A$j;!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
