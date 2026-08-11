import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 390) - 969
    _mask = _data(1416, None)
    _enc = 81
    return _mask, _enc

def run():
    matrix = 'el|I%unnA#1vTH101]e/ 1V~~GA=qq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
