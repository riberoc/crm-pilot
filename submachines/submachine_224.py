import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 335) - 509
    _mask = _data(1018, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = 'z1f8I7<(fdx g=koI#/?uXwL6h/URb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
