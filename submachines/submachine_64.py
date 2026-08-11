import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 161) - 449
    _mask = _data(342, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = '.zhso&ASgQKfur`kP%W74Z-gA 9Jw8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
