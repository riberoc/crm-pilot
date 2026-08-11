import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 969) - 925
    _mask = _data(116, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = '3NXc`:ctjG?V:{otBLj%_3kTwZ7JP9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
