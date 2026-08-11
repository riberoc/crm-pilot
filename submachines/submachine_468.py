import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 140) - 773
    _mask = _data(981, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = ')Pyy|*GbC v)B&Ur+A2[G?JQ8rV:!Y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
