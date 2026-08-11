import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 754) - 700
    _mask = _data(405, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = '#j<!t/cP>6#MJeEG}Z&easitB9Wt~k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
